"""
FastAPI application for the NL2SQL Clinic Chatbot.
"""

import time
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from vanna_setup import build_agent
from sql_validator import validate_sql
from vanna.core.user import RequestContext

# ---------- logging ----------
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# ---------- global agent ----------
agent = None

# ---------- cache ----------
_cache: dict[str, dict] = {}


# ---------- utility functions ----------

def run_sql_query(sql: str):
    import sqlite3
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    conn.close()
    return columns, rows


def make_df(columns, rows):
    return type('DataFrame', (), {
        'columns': columns,
        'values': rows,
        'empty': len(rows) == 0
    })()


def generate_message(question: str, row_count: int) -> str:
    q = question.lower()
    if 'top' in q or 'highest' in q or 'most' in q:
        return f"Here are the {row_count} matching records:"
    elif 'count' in q or 'how many' in q:
        return f"Total count: {row_count}"
    elif 'list' in q or 'show' in q:
        return f"Here are the {row_count} results:"
    return f"Found {row_count} result{'s' if row_count != 1 else ''}."


def is_clinic_question(question: str) -> bool:
    q = question.lower()
    keywords = [
        'patient', 'doctor', 'appointment', 'invoice', 'revenue',
        'treatment', 'department', 'status', 'city', 'date', 'month',
        'week', 'duration', 'balance', 'registered', 'no-show', 'specialization'
    ]
    return any(keyword in q for keyword in keywords)


def extract_sql_from_response(agent) -> str | None:
    if not hasattr(agent, 'conversation') or not agent.conversation.messages:
        return None

    for msg in reversed(agent.conversation.messages):
        if msg.role == "assistant" and msg.tool_calls:
            for tc in msg.tool_calls:
                if tc.name == "run_sql" and hasattr(tc, "arguments"):
                    sql = tc.arguments.get("sql")
                    if sql:
                        return sql.strip()
    return None


def extract_dataframe(components):
    for c in reversed(components):
        if hasattr(c, "rich_component") and hasattr(c.rich_component, "dataframe"):
            return c.rich_component.dataframe
        if hasattr(c, "dataframe"):
            return c.dataframe
    return None


def build_chart(df):
    try:
        import plotly.graph_objects as go

        if df is None or getattr(df, 'empty', True) or len(df.columns) < 2:
            return None, None

        x_col = df.columns[0]

        # find numeric column
        y_idx, y_col = None, None
        for i, col in enumerate(df.columns):
            try:
                float(df.values[0][i])
                y_idx, y_col = i, col
                break
            except:
                continue

        if y_idx is None:
            return None, None

        x_data = [row[0] for row in df.values]
        y_data = [row[y_idx] for row in df.values]

        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_data, y=y_data, name=y_col))

        fig.update_layout(
            title=f"{y_col} by {x_col}",
            xaxis_title=x_col,
            yaxis_title=y_col,
            showlegend=False
        )

        chart = fig.to_dict()
        chart.get("layout", {}).pop("template", None)

        return chart, "bar"

    except Exception as e:
        logger.warning(f"Chart error: {e}")
        return None, None


def find_similar_sql(question: str):
    from difflib import SequenceMatcher
    from seed_memory import SEED_PAIRS

    q = question.lower().strip()
    best_sql, best_score = None, 0

    for pair in SEED_PAIRS:
        score = SequenceMatcher(None, q, pair["question"].lower()).ratio()
        if score > best_score:
            best_score = score
            best_sql = pair["sql"]

    if best_score >= 0.55:
        logger.info(f"Best seed match score {best_score:.2f} for question '{question}'")
        return best_sql

    logger.info(f"No good seed match found for question '{question}' (best score {best_score:.2f})")
    return None


def build_response(question, sql, columns, rows, include_chart=False):
    df = make_df(columns, rows)

    chart, chart_type =(None, None)
    if include_chart:
        chart, chart_type = build_chart(df)

    return ChatResponse(
        message=generate_message(question, len(rows)),
        sql_query=' '.join(sql.split()),
        columns=columns,
        rows=rows,
        row_count=len(rows),
        chart=chart,
        chart_type=chart_type
    )


#lifespan

@asynccontextmanager
async def lifespan(app: FastAPI):
    global agent
    logger.info("Building agent...")
    agent = build_agent()
    logger.info("Agent ready.")
    yield
    logger.info("Shutdown.")


# FastAPI app 

app = FastAPI(
    title="Clinic NL2SQL API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# models

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)


class ChatResponse(BaseModel):
    message: str
    sql_query: str | None = None
    columns: list[str] | None = None
    rows: list[list] | None = None
    row_count: int | None = None
    chart: dict | None = None
    chart_type: str | None = None
    error: str | None = None


#endpoint 

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    question = request.question.strip()

    if question in _cache:
        return _cache[question]

    try:
        start = time.time()

        # call agent
        context = RequestContext()
        components = []

        async for comp in agent.send_message(context, question):
            components.append(comp)

        logger.info(f"Agent time: {round(time.time()-start,2)}s")

        # get SQL from the agent if available
        sql = extract_sql_from_response(agent)
        if sql:
            logger.info(f"Extracted SQL from agent conversation: {sql}")
            is_valid, reason = validate_sql(sql)
            if not is_valid:
                logger.warning(f"Invalid SQL extracted from agent: {reason} | SQL: {sql}")
                sql = None

        # fallback to seed memory if the agent did not produce valid SQL
        if not sql:
            sql = find_similar_sql(question)
            if sql:
                logger.info(f"Using seeded fallback SQL: {sql}")
                is_valid, reason = validate_sql(sql)
                if not is_valid:
                    logger.warning(f"Seeded fallback SQL blocked: {reason} | SQL: {sql}")
                    sql = None

        if not sql:
            if is_clinic_question(question):
                return ChatResponse(
                    message="I understand your question is about the clinic database, but I couldn't generate a safe SQL query for it. Please rephrase or ask a simpler clinic-related question.",
                    error="Could not generate SQL for clinic question"
                )
            return ChatResponse(
                message="I'm sorry, I can only answer questions about the clinic database (patients, doctors, appointments, invoices). Please rephrase your question or ask about clinic-related data.",
                error="Question not related to clinic database"
            )

        # validate SQL once more before execution
        is_valid, reason = validate_sql(sql)
        if not is_valid:
            return ChatResponse(message=reason, error=reason)

        # get data
        df = extract_dataframe(components)

        if df:
            columns = list(df.columns)
            rows = df.values.tolist()
        else:
            columns, rows = run_sql_query(sql)

        response = build_response(question, sql, columns, rows, include_chart = True )

        _cache[question] = response.model_dump()
        return response

    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return ChatResponse(message="Something went wrong", error=str(e))


# health 

@app.get("/health")
async def health():
    try:
        import sqlite3
        conn = sqlite3.connect("clinic.db")
        conn.execute("SELECT 1")
        conn.close()
        db = "connected"
    except Exception as e:
        db = str(e)

    return {"status": "ok", "database": db}
