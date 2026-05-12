from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Rezervacija(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    date: datetime
    time_begin: datetime
    duration_h: int
    teren_id: int  
    status: Optional[str] = "pending"

class RezervacijaCreate(SQLModel):
    user: str
    date: datetime
    time_begin: datetime
    duration_h: int
    teren_id: int
    status: Optional[str] = "pending"

class RezervacijaUpdate(SQLModel):
    user:       Optional[str] = None
    date:       Optional[datetime] = None
    time_begin: Optional[datetime] = None
    duration_h: Optional[int] = None
    teren_id:   Optional[int] = None
    status:     Optional[str] = None