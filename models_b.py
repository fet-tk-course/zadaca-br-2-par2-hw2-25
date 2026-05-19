from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import field_validator


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

    @field_validator("user")
    @classmethod
    def validate_user(cls, value):
        if not value[0].isupper():
            raise ValueError("Ime korisnika mora počinjati velikim slovom")
        return value

    @field_validator("duration_h")
    @classmethod
    def validate_duration(cls, value):
        if value < 1 or value > 4:
            raise ValueError("Trajanje mora biti između 1 i 4 sata")
        return value

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        allowed = ["pending", "confirmed", "cancelled"]
        if value not in allowed:
            raise ValueError("Status mora biti: pending, confirmed ili cancelled")
        return value


class RezervacijaUpdate(SQLModel):
    user: Optional[str] = None
    date: Optional[datetime] = None
    time_begin: Optional[datetime] = None
    duration_h: Optional[int] = None
    teren_id: Optional[int] = None
    status: Optional[str] = None

class ProvjeraTermina(SQLModel):
    date: datetime
    time_begin: datetime
    teren_id: int











    