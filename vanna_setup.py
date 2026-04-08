# vanna_setup.py
"""
Initializes the Vanna 2.0 Agent.

Vanna 2.0 uses an Agent architecture:
  - LLM Service   : the AI brain (Gemini here) that generates SQL
  - ToolRegistry  : tools the agent can call (run SQL, visualize data, etc.)
  - AgentMemory   : stores past successful Q&A pairs so agent learns
  - SqliteRunner  : built-in database runner (we don't write our own)
  - Agent         : ties everything together
"""

import os
from dotenv import load_dotenv
import logging

from vanna import Agent, AgentConfig
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.integrations.google import GeminiLlmService

load_dotenv()  # reads .env file for GOOGLE_API_KEY

# Setup logging
logger = logging.getLogger(__name__)


def build_agent() -> Agent:
    """
    Builds and returns a fully configured Vanna 2.0 Agent.
    Call this once at application startup.
    """

    # 1. LLM Service — the AI that reads your question and writes SQL
    llm_service = GeminiLlmService(
        api_key=os.environ["GOOGLE_API_KEY"],
        model="gemini-2.0-flash"
    )
    
    # Skip LLM test - the agent will handle errors gracefully

    # 2. Database runner — Vanna's built-in SQLite connector
    #    Pass the path to your database file
    db_runner = SqliteRunner(database_path="clinic.db")
    
    # Test database connection
    try:
        import sqlite3
        conn = sqlite3.connect("clinic.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM patients")
        patient_count = cursor.fetchone()[0]
        conn.close()
        logger.info(f"Database connection successful. Found {patient_count} patients.")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

    # 3. Agent Memory — stores correct Q&A pairs so the agent can learn
    #    DemoAgentMemory is the in-process memory store for Vanna 2.0
    agent_memory = DemoAgentMemory()
    logger.info("Agent memory initialized")

    # 4. Tool Registry — register every tool the agent is allowed to use
    registry = ToolRegistry()
    registry.register_local_tool(RunSqlTool(sql_runner=db_runner), access_groups=["admin", "user"])
    registry.register_local_tool(VisualizeDataTool(), access_groups=["admin", "user"])
    registry.register_local_tool(SaveQuestionToolArgsTool(), access_groups=["admin"])
    registry.register_local_tool(SearchSavedCorrectToolUsesTool(), access_groups=["admin", "user"])
    
    logger.info(f"Registered {len(registry._tools)} tools: {list(registry._tools.keys())}")

    # 5. User Resolver — identifies who is making the request
    #    For this project, everyone is treated as the same default user
    class DefaultUserResolver(UserResolver):
        async def resolve_user(self, context: RequestContext) -> User:
            # Return user with admin access to all tools
            return User(id="default_user", name="Clinic User", groups=["admin", "user"])

    user_resolver = DefaultUserResolver()

    # 6. Agent Config — tells the agent about the database schema
    #    The schema_description helps the LLM understand table structure
    config = AgentConfig(
        schema_description="""You are a SQL expert working with a clinic management database. 

DATABASE SCHEMA:
- patients(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT, phone TEXT, date_of_birth DATE, gender TEXT, city TEXT, registered_date DATE)
- doctors(id INTEGER PRIMARY KEY, name TEXT, specialization TEXT, department TEXT, phone TEXT)  
- appointments(id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appointment_date DATETIME, status TEXT, notes TEXT)
- treatments(id INTEGER PRIMARY KEY, appointment_id INTEGER, treatment_name TEXT, cost REAL, duration_minutes INTEGER)
- invoices(id INTEGER PRIMARY KEY, patient_id INTEGER, invoice_date DATE, total_amount REAL, paid_amount REAL, status TEXT)

RELATIONSHIPS:
- appointments.patient_id -> patients.id
- appointments.doctor_id -> doctors.id  
- treatments.appointment_id -> appointments.id
- invoices.patient_id -> patients.id

VALID VALUES:
- appointment.status: 'Scheduled', 'Completed', 'Cancelled', 'No-Show'
- invoice.status: 'Paid', 'Pending', 'Overdue'
- doctor.specialization: 'Dermatology', 'Cardiology', 'Orthopedics', 'General', 'Pediatrics'

Always write valid SQLite SQL queries. Use proper JOINs and aggregate functions when needed.""",
    )
    logger.info("Agent config created with detailed schema")

    # 7. Build the Agent — wire all components together
    agent = Agent(
        llm_service=llm_service,
        tool_registry=registry,
        agent_memory=agent_memory,
        user_resolver=user_resolver,
        config=config,
    )
    
    logger.info("Agent created successfully!")
    return agent

if __name__ == "__main__":
    agent = build_agent()
    print("✅ Agent created successfully!")
