from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    daily_entries = relationship("DailyEntry", back_populates="user")

class DailyEntry(Base):
    __tablename__ = "daily_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.utcnow)
    
    # Scales (1-10)
    mood_score = Column(Integer)
    energy_score = Column(Integer)
    productivity_score = Column(Integer)
    
    # Text responses
    mood_elaboration = Column(Text)
    energy_elaboration = Column(Text)
    productivity_elaboration = Column(Text)
    general_notes = Column(Text)
    
    # Sleep data
    sleep_time = Column(DateTime)
    wake_time = Column(DateTime)
    sleep_quality = Column(Integer)
    sleep_notes = Column(Text)
    
    user = relationship("User", back_populates="daily_entries")
    meals = relationship("MealEntry", back_populates="daily_entry")

class MealEntry(Base):
    __tablename__ = "meal_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    daily_entry_id = Column(Integer, ForeignKey("daily_entries.id"))
    meal_type = Column(String)  # breakfast, lunch, dinner, snack
    time = Column(DateTime)
    description = Column(Text)
    satisfaction_score = Column(Integer)  # 1-10 scale
    
    daily_entry = relationship("DailyEntry", back_populates="meals")