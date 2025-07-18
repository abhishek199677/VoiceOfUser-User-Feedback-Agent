import sqlite3
from typing import List
from datetime import datetime

DB_NAME = "feedback.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            business_id TEXT,
            rating INTEGER,
            comment TEXT,
            metadata TEXT,
            timestamp TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            business_id TEXT PRIMARY KEY,
            summary TEXT,
            last_updated TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_feedback(data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO feedback (user_id, business_id, rating, comment, metadata, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.user_id,
        data.business_id,
        data.rating,
        data.comment,
        str(data.metadata),
        data.timestamp.isoformat()
    ))
    conn.commit()
    conn.close()

def fetch_feedback_by_business(business_id: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT comment FROM feedback WHERE business_id = ?", (business_id,))
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]
