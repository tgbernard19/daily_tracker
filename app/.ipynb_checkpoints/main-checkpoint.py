from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models
from .database import engine, get_db
from .models import models

# Create FastAPI app
app = FastAPI(
    title="Daily Tracker API",
    description="API for tracking daily metrics and generating insights",
    version="1.0.0"
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Daily Tracker API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# More endpoints to be added here