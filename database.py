import sqlite3


DATABASE = "database/loan.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            income REAL,
            credit_score INTEGER,
            existing_loan TEXT,
            repayment_history TEXT,
            decision TEXT,
            risk_level TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_application(
    age,
    income,
    credit_score,
    existing_loan,
    repayment_history,
    decision,
    risk_level
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO applications
        (age, income, credit_score, existing_loan,
         repayment_history, decision, risk_level)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        age,
        income,
        credit_score,
        existing_loan,
        repayment_history,
        decision,
        risk_level
    ))

    conn.commit()
    conn.close()
    
def get_applications():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM applications
        ORDER BY id DESC
    """)

    applications = cursor.fetchall()

    conn.close()

    return applications    