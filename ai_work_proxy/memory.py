import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            plan TEXT,
            output_file TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_task(task, plan, output_file):
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO tasks (task, plan, output_file, timestamp)
        VALUES (?, ?, ?, ?)
    """, (task, plan, output_file, str(datetime.now())))
    conn.commit()
    conn.close()