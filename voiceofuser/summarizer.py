import os
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3
from datetime import datetime
from database import DB_NAME

load_dotenv()

# ✅ Use new client constructor for OpenAI >= 1.0
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(feedbacks):
    prompt = "Summarize the following user feedback for actionable insights:\n\n" + "\n".join(feedbacks)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes user feedback for hospitality businesses."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            "summary": response.choices[0].message.content.strip(),
            "last_updated": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "summary": f"Error during summarization: {str(e)}",
            "last_updated": None
        }

def save_summary(business_id, summary_data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("REPLACE INTO summaries (business_id, summary, last_updated) VALUES (?, ?, ?)",
                (business_id, summary_data["summary"], summary_data["last_updated"]))
    conn.commit()
    conn.close()

def get_summary(business_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT summary, last_updated FROM summaries WHERE business_id = ?", (business_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"summary": row[0], "last_updated": row[1]}
    return None
