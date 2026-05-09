from sqlmodel import SQLModel, Field
from typing import Optional

class Rezervacija(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    date: str
    time_begin: str
    duration_h: int
    teren_id: int  # veza na Teren model
    status: Optional[str] = "pending"

class RezervacijaCreate(SQLModel):
    user: str
    date: str
    time_begin: str
    duration_h: int
    teren_id: int


class RezervacijaUpdate(SQLModel):
    user:       Optional[str] = None
    date:       Optional[str] = None
    time_begin: Optional[str] = None
    duration_h: Optional[int] = None
    teren_id:   Optional[int] = None
    status:     Optional[str] = None