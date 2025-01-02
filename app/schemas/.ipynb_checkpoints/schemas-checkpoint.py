from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str  # Password in plain text (only for user creation)

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model

# Daily Entry Schemas
class DailyEntryCreate(BaseModel):
    # Scales with validation
    mood_score: int = Field(..., ge=1, le=10)  # Must be between 1 and 10
    energy_score: int = Field(..., ge=1, le=10)
    productivity_score: int = Field(..., ge=1, le=10)
    
    # Optional text fields
    mood_elaboration: Optional[str] = None
    energy_elaboration: Optional[str] = None
    productivity_elaboration: Optional[str] = None
    general_notes: Optional[str] = None
    
    # Sleep data
    sleep_time: datetime
    wake_time: datetime
    sleep_quality: int = Field(..., ge=1, le=10)
    sleep_notes: Optional[str] = None
    
    @validator('wake_time')
    def wake_time_must_be_after_sleep_time(cls, v, values):
        if 'sleep_time' in values and v <= values['sleep_time']:
            raise ValueError('wake_time must be after sleep_time')
        return v

class DailyEntry(DailyEntryCreate):
    id: int
    user_id: int
    date: datetime
    
    class Config:
        from_attributes = True

# Meal Entry Schemas
class MealEntryCreate(BaseModel):
    meal_type: str = Field(..., regex='^(breakfast|lunch|dinner|snack)$')
    time: datetime
    description: str
    satisfaction_score: int = Field(..., ge=1, le=10)

class MealEntry(MealEntryCreate):
    id: int
    daily_entry_id: int
    
    class Config:
        from_attributes = True