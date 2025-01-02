from .schemas import * 
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True

# Daily Entry Schemas
class DailyEntryBase(BaseModel):
    mood_score: int = Field(..., ge=1, le=10)
    energy_score: int = Field(..., ge=1, le=10)
    productivity_score: int = Field(..., ge=1, le=10)
    mood_elaboration: Optional[str] = None
    energy_elaboration: Optional[str] = None
    productivity_elaboration: Optional[str] = None
    general_notes: Optional[str] = None
    sleep_time: datetime
    wake_time: datetime
    sleep_quality: int = Field(..., ge=1, le=10)
    sleep_notes: Optional[str] = None

class DailyEntryCreate(DailyEntryBase):
    pass

class DailyEntry(DailyEntryBase):
    id: int
    user_id: Optional[int] = None
    date: datetime
    
    class Config:
        from_attributes = True

# Make sure these are explicitly exported
__all__ = ['UserBase', 'UserCreate', 'User', 
           'DailyEntryBase', 'DailyEntryCreate', 'DailyEntry']