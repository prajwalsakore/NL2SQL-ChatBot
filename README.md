Hey Team Cogninest, i really appreciate what you are doing in AI and Data Industry. It will be privilage to working with you if got chance. Let's be honest, i am a Data Analyst fresher who is looking for job in data analyst, but iam also interested in AI and ML. I filled the form of AI ML role hoping i will get one chance of interview with you. During building this project I took help from AI tools, ironic! and also got help from github copilot. And to be honest all code i took from AI and then modified according to need. I think i need this role deperately that's why i did all i could have to complete this one. Yes, i copied code but i can say what every line of code do and how and why. So here is my results for each questions you mentioned in assignment file.

-- I must say i am quick learner and great at figuring out things. And if got chance as intern i will definetly thrive in this role and will be valuable asset for company for sure. 

--There must be some errors in readme.md files as this is my first end to end project in field of AI ML using Fastapi. I will learn it quickly in good learning environment. 

--Thanks Team Cogninest to give me opportunity to submit this end to end project which help me alot to learn new things in this field. I don't know what future hold but i will always dream to work with you.


--Here are project description and setup instructions.

This system converts natural language questions into SQL queries using 
Vanna AI 2.0 and Google Gemini. It is built on top of a simulated clinic 
database containing patients, doctors, appointments, treatments, and invoices.
The system is exposed as a REST API built with FastAPI.

-- What this project does
Accepts a plain English question via a POST request
Sends the question to Google Gemini (via Vanna 2.0 Agent)
Gemini generates a SQL query based on the clinic database schema
The SQL is validated for safety (SELECT only — no dangerous operations)
The query runs against a local SQLite database


---

## Setup Instructions

Follow these steps in order. Do not skip any step.

### Prerequisites

Before starting, make sure you have:
- Python 3.10 or higher installed
- A Google account (to get the free Gemini API key)
- VS Code or any code editor
- Git (optional, for cloning)

---

### Step 1 — Get Your Free Gemini API Key

1. Go to [aistudio.google.com](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key — you will need it in Step 4

---

### Step 2 — Download or Clone the Project

**Option A — Clone with Git:**
```bash
git clone [github.com](https://github.com/YOUR_USERNAME/clinic-nl2sql.git)
cd clinic-nl2sql


--Setup Instructions
Install Dependencies
pip install -r requirements.txt


Create Your .env File
GOOGLE_API_KEY=your_actual_gemini_key_here

Create the Database
python setup_database.py

Seed Agent Memory
python seed_memory.py

Start the API Server
uvicorn main:app --port 8000 --reload

Run Everything in One Command
pip install -r requirements.txt && python setup_database.py \
  && python seed_memory.py && uvicorn main:app --port 8000

How to Start the API Server
uvicorn main:app --port 8000 --reload

API Documentation
Endpoint 1 — POST /chat
Converts a natural language question into SQL, executes it,
and returns the results with an optional chart.

URL: POST [localhost](http://localhost:8000/chat)

Example 1 — Count Query

Request:

json


{
  "question": "How many patients do we have?"
}
Response:

json


{
  "message": "Total count: 1",
  "sql_query": "SELECT COUNT(*) AS total_patients FROM patients",
  "columns": ["total_patients"],
  "rows": [[200]],
  "row_count": 1,
  "chart": null,
  "chart_type": null,
  "error": null
}

Endpoint 2 — GET /health
Checks if the server, database, and agent memory are working correctly.
Use this to confirm the system is running before sending questions.

URL: GET [localhost](http://localhost:8000/health)

No request body needed.

Response:

json


{
  "status": "ok",
  "database": "connected",
  "agent_memory_items": 15
}



Architecture Overview

User (plain English question)
            │
            ▼
    ┌──────────────────┐
    │   FastAPI /chat  │  ← main.py
    │                  │
    │  1. Check cache  │
    │  2. Validate     │
    │     input        │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────────────────┐
    │     Vanna 2.0 Agent          │  ← vanna_setup.py
    │                              │
    │  ┌─────────────────────┐     │
    │  │ SearchMemoryTool    │     │
    │  │ "seen this before?" │     │
    │  └─────────────────────┘     │
    │            │                 │
    │            ▼                 │
    │  ┌─────────────────────┐     │
    │  │  GeminiLlmService   │     │
    │  │  generates SQL      │     │
    │  └─────────────────────┘     │
    │            │                 │
    │            ▼                 │
    │  ┌─────────────────────┐     │
    │  │  SaveMemoryTool     │     │
    │  │  learns from this   │     │
    │  └─────────────────────┘     │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────┐
    │   sql_validator.py   │  ← Security layer
    │                      │
    │  SELECT only?  ✓     │
    │  No DROP/DELETE? ✓   │
    │  No system tables? ✓ │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │   SqliteRunner       │  ← Vanna built-in
    │   runs query on      │
    │   clinic.db          │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │   Plotly Chart       │
    │   (if applicable)    │
    └──────────┬───────────┘
               │
               ▼
    JSON Response to User
    {sql, columns, rows, chart}

