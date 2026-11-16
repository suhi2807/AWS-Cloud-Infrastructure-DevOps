from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Cloud Infrastructure Health Monitor",
    description="A DevOps project for monitoring application health",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Cloud Infrastructure Health Monitor",
        "status": "Running",
        "project": "AWS Cloud Infrastructure and DevOps"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "server": "online",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
