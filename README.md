# VoiceOfUser - User Feedback Agent


# 🔍 Project Overview
VoiceOfUser is an AI-powered feedback agent built with FastAPI, designed to help hospitality businesses collect, store, and automatically summarize user feedback. It uses OpenAI GPT models to generate actionable summaries that help businesses quickly understand customer sentiment.

# 🚀 Features
✅ Feedback Collection API – Users can submit feedback via a simple POST endpoint

✅ Summarization with OpenAI – Automatically generates summaries from collected feedback

✅ Admin-Only Access – Secure summary access with Basic Authentication

✅ Lightweight Database – Feedback and summaries are stored using SQLite

✅ Swagger UI – Interactive API documentation available at /docs

# 💡 Tech Stack

Backend API -	FastAPI (Python)
AI Engine -	OpenAI GPT-3.5 (via SDK)
Auth	Basic Authentication
Storage	SQLite (lightweight DB)
Deployment -	Uvicorn (local/dev), Docker-ready

# 📦 API Endpoints

### Method	Endpoint	Description	Auth

GET	/summary	Get feedback summary	


# 🔐 Admin Credentials

Username: admin

Password: admin123


# Set your OpenAI key
echo "OPENAI_API_KEY=your-key" > .env


# 📌 Use Cases

Hospitality startups collecting guest feedback

Instant AI summarization for product/service reviews

Business admins reviewing user sentiment without reading all comments

# ✅ Future Enhancements

JWT or OAuth-based authentication

React or HTML frontend for feedback submission

Admin dashboard with charts/analytics

Support for other domains (e.g., healthcare, e-commerce)




<!-- {
  "user_id": "u1",
  "business_id": "hotel123",
  "rating": 5,
  "comment": "The staff was very friendly and rooms were clean.",
  "metadata": {
    "visit_date": "2025-07-10"
  }
} -->



<!-- docker stop fastapi-app   #stop
docker rm fastapi-app   #remove -->


