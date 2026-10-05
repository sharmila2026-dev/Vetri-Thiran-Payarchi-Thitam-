import uvicorn
from fastapi import FastAPI
from backend.routes import router

# Initialize the FastAPI application
app = FastAPI(
    title="LegalEase AI Legal Document Generator",
    description="API for generating, editing, and exporting AI-powered legal documents using Gemini 1.5 Pro.",
    version="1.0.0"
)

# Include the API router from routes.py
app.include_router(router)

# Base route to verify the API status
@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "Welcome to LegalEase AI Legal Document Generator API"
    }

# Entry point for running the server directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
