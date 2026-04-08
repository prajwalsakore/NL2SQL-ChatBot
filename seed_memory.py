# seed_memory.py
"""
Seeds the Vanna 2.0 Agent Memory with 15 known good Q&A pairs.

Why do this?
  Without any examples, the agent has to guess SQL from scratch every time.
  By giving it 15 correct examples upfront, it can find similar past queries
  and use them as reference — like giving a new employee a cheat sheet.

In Vanna 2.0, seeding works by calling agent.send_message() with a real question,
then storing the correct SQL in memory via SaveQuestionToolArgsTool.
Alternatively, we can directly populate DemoAgentMemory with known pairs.
"""

from vanna_setup import build_agent
from vanna.integrations.local.agent_memory import DemoAgentMemory
import asyncio
from vanna.core.user import RequestContext, User
from vanna.core import ToolContext
import uuid

# These are the 15 known-good question → SQL pairs
SEED_PAIRS = [
    {
        "question": "How many patients do we have?",
        "sql": "SELECT COUNT(*) AS total_patients FROM patients"
    },
    {
        "question": "List all doctors and their specializations",
        "sql": "SELECT name, specialization, department FROM doctors ORDER BY specialization"
    },
    {
        "question": "Which doctor has the most appointments?",
        "sql": """
            SELECT d.name, COUNT(a.id) AS appointment_count
            FROM doctors d
            JOIN appointments a ON a.doctor_id = d.id
            GROUP BY d.id, d.name
            ORDER BY appointment_count DESC
            LIMIT 1
        """
    },
    {
        "question": "What is the total revenue?",
        "sql": "SELECT SUM(total_amount) AS total_revenue FROM invoices"
    },
    {
        "question": "Show revenue by doctor",
        "sql": """
            SELECT d.name, SUM(i.total_amount) AS total_revenue
            FROM invoices i
            JOIN appointments a ON a.patient_id = i.patient_id
            JOIN doctors d ON d.id = a.doctor_id
            GROUP BY d.name
            ORDER BY total_revenue DESC
        """
    },
    {
        "question": "Which city has the most patients?",
        "sql": """
            SELECT city, COUNT(*) AS patient_count
            FROM patients
            GROUP BY city
            ORDER BY patient_count DESC
            LIMIT 1
        """
    },
    {
        "question": "Show me cancelled appointments",
        "sql": """
            SELECT a.id, p.first_name, p.last_name, a.appointment_date, a.status
            FROM appointments a
            JOIN patients p ON p.id = a.patient_id
            WHERE a.status = 'Cancelled'
            ORDER BY a.appointment_date DESC
        """
    },
    {
        "question": "Top 5 patients by total spending",
        "sql": """
            SELECT p.first_name, p.last_name, SUM(i.total_amount) AS total_spending
            FROM patients p
            JOIN invoices i ON i.patient_id = p.id
            GROUP BY p.id, p.first_name, p.last_name
            ORDER BY total_spending DESC
            LIMIT 5
        """
    },
    {
        "question": "Show unpaid invoices",
        "sql": """
            SELECT p.first_name, p.last_name, i.invoice_date, i.total_amount, i.paid_amount, i.status
            FROM invoices i
            JOIN patients p ON p.id = i.patient_id
            WHERE i.status IN ('Pending', 'Overdue')
            ORDER BY i.invoice_date DESC
        """
    },
    {
        "question": "List patients who visited more than 3 times",
        "sql": """
            SELECT p.first_name, p.last_name, COUNT(a.id) AS visit_count
            FROM patients p
            JOIN appointments a ON a.patient_id = p.id
            GROUP BY p.id, p.first_name, p.last_name
            HAVING COUNT(a.id) > 3
            ORDER BY visit_count DESC
        """
    },
    {
        "question": "Average treatment cost by specialization",
        "sql": """
            SELECT d.specialization, ROUND(AVG(t.cost), 2) AS avg_cost
            FROM treatments t
            JOIN appointments a ON a.id = t.appointment_id
            JOIN doctors d ON d.id = a.doctor_id
            GROUP BY d.specialization
            ORDER BY avg_cost DESC
        """
    },
    {
        "question": "Show monthly appointment count for the past 6 months",
        "sql": """
            SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) AS count
            FROM appointments
            WHERE appointment_date >= date('now', '-6 months')
            GROUP BY month
            ORDER BY month
        """
    },
    {
        "question": "Show the busiest day of the week for appointments",
        "sql": """
            SELECT
                CASE strftime('%w', appointment_date)
                    WHEN '0' THEN 'Sunday'
                    WHEN '1' THEN 'Monday'
                    WHEN '2' THEN 'Tuesday'
                    WHEN '3' THEN 'Wednesday'
                    WHEN '4' THEN 'Thursday'
                    WHEN '5' THEN 'Friday'
                    WHEN '6' THEN 'Saturday'
                END AS weekday,
                COUNT(*) AS appointment_count
            FROM appointments
            GROUP BY weekday
            ORDER BY appointment_count DESC
            LIMIT 1
        """
    },
    {
        "question": "Revenue trend by month",
        "sql": """
            SELECT strftime('%Y-%m', invoice_date) AS month, SUM(total_amount) AS total_revenue
            FROM invoices
            GROUP BY month
            ORDER BY month
        """
    },
    {
        "question": "Average appointment duration by doctor",
        "sql": """
            SELECT d.name, ROUND(AVG(t.duration_minutes), 2) AS avg_duration
            FROM treatments t
            JOIN appointments a ON a.id = t.appointment_id
            JOIN doctors d ON d.id = a.doctor_id
            GROUP BY d.id, d.name
            ORDER BY avg_duration DESC
        """
    },
    {
        "question": "Compare revenue between departments",
        "sql": """
            SELECT d.department, SUM(i.total_amount) AS total_revenue
            FROM invoices i
            JOIN appointments a ON a.patient_id = i.patient_id
            JOIN doctors d ON d.id = a.doctor_id
            GROUP BY d.department
            ORDER BY total_revenue DESC
        """
    },
    {
        "question": "What percentage of appointments are no-shows?",
        "sql": """
            SELECT
                ROUND(
                    100.0 * SUM(CASE WHEN status = 'No-Show' THEN 1 ELSE 0 END) / COUNT(*),
                    2
                ) AS no_show_percentage
            FROM appointments
        """
    },
    {
        "question": "Show patient registration trend by month",
        "sql": """
            SELECT strftime('%Y-%m', registered_date) AS month, COUNT(*) AS new_patients
            FROM patients
            GROUP BY month
            ORDER BY month
        """
    },
    {
        "question": "List patients with overdue invoices",
        "sql": """
            SELECT DISTINCT p.first_name, p.last_name, p.email, p.phone,
                   i.total_amount, i.paid_amount, i.status
            FROM patients p
            JOIN invoices i ON i.patient_id = p.id
            WHERE i.status = 'Overdue'
            ORDER BY i.total_amount DESC
        """
    },
]


async def seed():
    print("Building agent...")
    agent = build_agent()

    print(f"Seeding {len(SEED_PAIRS)} Q&A pairs into agent memory...")

    # Access the DemoAgentMemory directly and store each pair
    # All AgentMemory methods are async, so we need a ToolContext
    memory: DemoAgentMemory = agent.agent_memory
    
    # Create a user context for seeding
    user = User(id="seed_user", name="Seed User")
    
    # Create a ToolContext for saving
    tool_context = ToolContext(
        user=user,
        conversation_id="seed_conversation",
        request_id=str(uuid.uuid4()),
        agent_memory=memory
    )

    for i, pair in enumerate(SEED_PAIRS, 1):
        # Save as successful RunSqlTool usage
        await memory.save_tool_usage(
            question=pair["question"],
            tool_name="run_sql",
            args={"sql": pair["sql"].strip()},
            context=tool_context,
            success=True,
            metadata={"source": "seed"}
        )
        print(f"  [{i}/{len(SEED_PAIRS)}] Seeded: {pair['question'][:60]}")

    print(f"\nAgent memory seeded with {len(SEED_PAIRS)} examples.")
    print("The agent will use these as reference when answering similar questions.")


if __name__ == "__main__":
    asyncio.run(seed())
