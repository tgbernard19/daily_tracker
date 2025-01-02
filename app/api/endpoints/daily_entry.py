from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, date

from ...database import get_db
from ... import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.DailyEntry)
def create_daily_entry(entry: schemas.DailyEntryCreate, db: Session = Depends(get_db)):
    """Create a new daily entry."""
    db_entry = models.DailyEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/{entry_id}", response_model=schemas.DailyEntry)
def read_daily_entry(entry_id: int, db: Session = Depends(get_db)):
    """Get a specific daily entry."""
    db_entry = db.query(models.DailyEntry).filter(models.DailyEntry.id == entry_id).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@router.get("/by-date/{date}", response_model=schemas.DailyEntry)
def read_entry_by_date(date: date, db: Session = Depends(get_db)):
    """Get entry for a specific date."""
    db_entry = db.query(models.DailyEntry).filter(
        models.DailyEntry.date >= date,
        models.DailyEntry.date < date + timedelta(days=1)
    ).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="No entry found for this date")
    return db_entry

@router.put("/{entry_id}", response_model=schemas.DailyEntry)
def update_daily_entry(entry_id: int, entry: schemas.DailyEntryCreate, db: Session = Depends(get_db)):
    """Update a daily entry."""
    db_entry = db.query(models.DailyEntry).filter(models.DailyEntry.id == entry_id).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    
    db.commit()
    db.refresh(db_entry)
    return db_entry