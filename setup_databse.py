# setup_database.py
"""
Creates the clinic.db SQLite database with schema and dummy data.
Run this first before anything else.
"""

import sqlite3
import random
from datetime import datetime, timedelta, date

# ---------- helpers ----------

def random_date(start: date, end: date) -> str:
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).isoformat()

def random_datetime(start: date, end: date) -> str:
    base = datetime(start.year, start.month, start.day, 8, 0, 0)
    delta_days = (end - start).days
    minutes_offset = random.randint(0, delta_days * 24 * 60)
    return (base + timedelta(minutes=minutes_offset)).strftime("%Y-%m-%d %H:%M:%S")

# ---------- data pools ----------

FIRST_NAMES = [
    "Aarav", "Priya", "Rahul", "Sneha", "Arjun", "Neha", "Vikram", "Ananya",
    "Rohan", "Pooja", "Aditya", "Divya", "Karan", "Meera", "Siddharth",
    "Kavya", "Amit", "Isha", "Nikhil", "Shreya", "Yash", "Riya", "Harsh",
    "Tanvi", "Varun", "Naina", "Kunal", "Simran", "Ayaan", "Tara",
    "Deepak", "Ankita", "Rajesh", "Swati", "Manish", "Preeti", "Suresh",
    "Geeta", "Pankaj", "Sunita", "Abhishek", "Rekha", "Vijay", "Usha",
    "Sanjay", "Lata", "Manoj", "Kavita", "Dinesh", "Asha"
]

LAST_NAMES = [
    "Sharma", "Patel", "Singh", "Mehta", "Gupta", "Joshi", "Nair", "Iyer",
    "Reddy", "Shah", "Kumar", "Verma", "Mishra", "Pandey", "Chopra",
    "Malhotra", "Kapoor", "Bose", "Das", "Rao"
]

CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"
]

DOCTOR_NAMES = [
    "Dr. Arun Kapoor", "Dr. Meena Pillai", "Dr. Sameer Joshi",
    "Dr. Reena Shah", "Dr. Ankit Malhotra", "Dr. Priti Nair",
    "Dr. Suresh Iyer", "Dr. Kavita Reddy", "Dr. Rahul Bose",
    "Dr. Sunita Pandey", "Dr. Vijay Mehta", "Dr. Neha Gupta",
    "Dr. Rajesh Sharma", "Dr. Divya Singh", "Dr. Manish Verma"
]

SPECIALIZATIONS = [
    "Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"
]

DEPARTMENTS = {
    "Dermatology": "Skin Care",
    "Cardiology": "Heart & Vascular",
    "Orthopedics": "Bone & Joint",
    "General": "General Medicine",
    "Pediatrics": "Child Health"
}

TREATMENT_NAMES = {
    "Dermatology": ["Skin Biopsy", "Acne Treatment", "Laser Therapy", "Eczema Care"],
    "Cardiology": ["ECG", "Angioplasty", "Cardiac Stress Test", "Echo Cardiogram"],
    "Orthopedics": ["Physiotherapy", "Joint Replacement", "Fracture Treatment", "Bone Scan"],
    "General": ["General Checkup", "Blood Test", "Vaccination", "Flu Treatment"],
    "Pediatrics": ["Child Vaccination", "Growth Monitoring", "Pediatric Checkup", "Allergy Test"]
}

STATUSES_APPOINTMENT = ["Scheduled", "Completed", "Cancelled", "No-Show"]
STATUSES_INVOICE = ["Paid", "Pending", "Overdue"]


def create_schema(cursor: sqlite3.Cursor) -> None:
    cursor.executescript("""
        DROP TABLE IF EXISTS invoices;
        DROP TABLE IF EXISTS treatments;
        DROP TABLE IF EXISTS appointments;
        DROP TABLE IF EXISTS doctors;
        DROP TABLE IF EXISTS patients;

        CREATE TABLE patients (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name      TEXT NOT NULL,
            last_name       TEXT NOT NULL,
            email           TEXT,
            phone           TEXT,
            date_of_birth   DATE,
            gender          TEXT,
            city            TEXT,
            registered_date DATE
        );

        CREATE TABLE doctors (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT NOT NULL,
            specialization   TEXT,
            department       TEXT,
            phone            TEXT
        );

        CREATE TABLE appointments (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id       INTEGER REFERENCES patients(id),
            doctor_id        INTEGER REFERENCES doctors(id),
            appointment_date DATETIME,
            status           TEXT,
            notes            TEXT
        );

        CREATE TABLE treatments (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_id   INTEGER REFERENCES appointments(id),
            treatment_name   TEXT,
            cost             REAL,
            duration_minutes INTEGER
        );

        CREATE TABLE invoices (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id    INTEGER REFERENCES patients(id),
            invoice_date  DATE,
            total_amount  REAL,
            paid_amount   REAL,
            status        TEXT
        );
    """)


def insert_doctors(cursor: sqlite3.Cursor) -> list[int]:
    """Insert 15 doctors across 5 specializations (3 each)."""
    doctor_ids = []
    for i, name in enumerate(DOCTOR_NAMES):
        spec = SPECIALIZATIONS[i // 3]  # 3 doctors per specialization
        dept = DEPARTMENTS[spec]
        phone = f"98{random.randint(10000000, 99999999)}"
        cursor.execute(
            "INSERT INTO doctors (name, specialization, department, phone) VALUES (?,?,?,?)",
            (name, spec, dept, phone)
        )
        doctor_ids.append(cursor.lastrowid)
    return doctor_ids


def insert_patients(cursor: sqlite3.Cursor) -> list[int]:
    """Insert 200 patients spread across 10 cities."""
    today = date.today()
    start_dob = date(1950, 1, 1)
    end_dob = date(2005, 12, 31)
    reg_start = today - timedelta(days=365 * 3)

    patient_ids = []
    for _ in range(200):
        fn = random.choice(FIRST_NAMES)
        ln = random.choice(LAST_NAMES)
        # Some patients have no email/phone (NULL), makes data realistic
        email = f"{fn.lower()}.{ln.lower()}{random.randint(1,99)}@email.com" if random.random() > 0.15 else None
        phone = f"91{random.randint(6000000000, 9999999999)}" if random.random() > 0.10 else None
        dob = random_date(start_dob, end_dob)
        gender = random.choice(["M", "F"])
        city = random.choice(CITIES)
        reg_date = random_date(reg_start, today)

        cursor.execute("""
            INSERT INTO patients
              (first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
            VALUES (?,?,?,?,?,?,?,?)
        """, (fn, ln, email, phone, dob, gender, city, reg_date))
        patient_ids.append(cursor.lastrowid)

    return patient_ids


def insert_appointments(
    cursor: sqlite3.Cursor,
    patient_ids: list[int],
    doctor_ids: list[int]
) -> list[tuple[int, int]]:
    """
    Insert 500 appointments over the past 12 months.
    Returns list of (appointment_id, doctor_id) for completed appointments.
    """
    today = date.today()
    start = today - timedelta(days=365)

    # Make some patients heavy users, some light — realistic distribution
    # 30 patients get many appointments, rest get 1-2
    heavy_patients = random.sample(patient_ids, 30)
    heavy_weight = 8   # avg appointments for heavy users
    light_weight = 1

    appointments_to_insert = []
    for pid in patient_ids:
        count = random.randint(5, heavy_weight) if pid in heavy_patients else random.randint(1, 3)
        for _ in range(count):
            appointments_to_insert.append(pid)

    # Trim or pad to exactly 500
    random.shuffle(appointments_to_insert)
    appointments_to_insert = appointments_to_insert[:500]
    while len(appointments_to_insert) < 500:
        appointments_to_insert.append(random.choice(patient_ids))

    # Some doctors are busier than others
    doctor_weights = [random.randint(1, 10) for _ in doctor_ids]

    completed_appointments = []  # (appointment_id, doctor_id) tuples

    for pid in appointments_to_insert:
        did = random.choices(doctor_ids, weights=doctor_weights, k=1)[0]
        appt_dt = random_datetime(start, today)
        status = random.choices(
            STATUSES_APPOINTMENT,
            weights=[10, 50, 25, 15],  # Completed is most common
            k=1
        )[0]
        notes = f"Follow-up required." if random.random() > 0.6 else None

        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
            VALUES (?,?,?,?,?)
        """, (pid, did, appt_dt, status, notes))

        appt_id = cursor.lastrowid

        if status == "Completed":
            completed_appointments.append((appt_id, did))

    return completed_appointments


def insert_treatments(
    cursor: sqlite3.Cursor,
    completed_appointments: list[tuple[int, int]],
    doctor_ids: list[int]
) -> None:
    """Insert up to 350 treatments for completed appointments."""
    # Get doctor specialization mapping
    cursor.execute("SELECT id, specialization FROM doctors")
    doc_spec = {row[0]: row[1] for row in cursor.fetchall()}

    sample = random.sample(
        completed_appointments,
        min(350, len(completed_appointments))
    )

    for appt_id, doc_id in sample:
        spec = doc_spec.get(doc_id, "General")
        treatment = random.choice(TREATMENT_NAMES.get(spec, ["General Checkup"]))
        cost = round(random.uniform(50, 5000), 2)
        duration = random.randint(15, 120)

        cursor.execute("""
            INSERT INTO treatments (appointment_id, treatment_name, cost, duration_minutes)
            VALUES (?,?,?,?)
        """, (appt_id, treatment, cost, duration))


def insert_invoices(
    cursor: sqlite3.Cursor,
    patient_ids: list[int]
) -> None:
    """Insert 300 invoices with mix of Paid, Pending, Overdue."""
    today = date.today()
    start = today - timedelta(days=365)

    selected_patients = random.choices(patient_ids, k=300)

    for pid in selected_patients:
        inv_date = random_date(start, today)
        total = round(random.uniform(200, 8000), 2)
        status = random.choices(
            STATUSES_INVOICE,
            weights=[50, 30, 20],
            k=1
        )[0]

        if status == "Paid":
            paid = total
        elif status == "Pending":
            paid = round(random.uniform(0, total * 0.5), 2)
        else:  # Overdue
            paid = round(random.uniform(0, total * 0.3), 2)

        cursor.execute("""
            INSERT INTO invoices (patient_id, invoice_date, total_amount, paid_amount, status)
            VALUES (?,?,?,?,?)
        """, (pid, inv_date, total, paid, status))


def main():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    print("Creating schema...")
    create_schema(cursor)

    print("Inserting doctors...")
    doctor_ids = insert_doctors(cursor)

    print("Inserting patients...")
    patient_ids = insert_patients(cursor)

    print("Inserting appointments...")
    completed = insert_appointments(cursor, patient_ids, doctor_ids)

    print("Inserting treatments...")
    insert_treatments(cursor, completed, doctor_ids)

    print("Inserting invoices...")
    insert_invoices(cursor, patient_ids)

    conn.commit()

    # Print summary
    for table in ["patients", "doctors", "appointments", "treatments", "invoices"]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} records")

    conn.close()
    print("\nclinic.db created successfully!")


if __name__ == "__main__":
    main()
