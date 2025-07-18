from models import FeedbackModel
from database import init_db, save_feedback, fetch_feedback_by_business
from summarizer import generate_summary, save_summary, get_summary
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


init_db()

app = FastAPI()
security = HTTPBasic()


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    

@app.get("/")
def root():
    return {"message": "VoiceOfUser API is running. Visit /docs for API documentation."}

@app.post("/feedback")
def submit_feedback(feedback: FeedbackModel):
    save_feedback(feedback)
    return {"message": "Feedback submitted successfully"}

@app.get("/summary")
def get_feedback_summary(business_id: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
    summary = get_summary(business_id)
    if summary:
        return summary

    feedbacks = fetch_feedback_by_business(business_id)
    if not feedbacks:
        raise HTTPException(status_code=404, detail="No feedback found")
    summary = generate_summary(feedbacks)
    save_summary(business_id, summary)
    return summary