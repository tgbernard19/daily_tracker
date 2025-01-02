from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import daily_entry

app = FastAPI(
    title="Daily Tracker API",
    description="API for tracking daily metrics and generating insights",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(
    daily_entry.router,
    prefix="/api/daily-entries",
    tags=["daily-entries"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Daily Tracker API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}