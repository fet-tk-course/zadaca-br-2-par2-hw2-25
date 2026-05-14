from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

class Teren(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surface: str
    capacity: int
    price_per_hour: float
    is_covered: bool
    available: bool = Field(default=True)

class TerenCreate(SQLModel):
    name: str
    surface: str
    capacity: int
    price_per_hour: float
    is_covered: bool
    available: bool = True

    @field_validator('name')
    @classmethod
    def naziv_ne_smije_biti_prazan(cls, naziv):
        if naziv.strip():
            raise ValueError('Naziv ne smije biti prazan string')
        return naziv.strip() 

class TerenUpdate(SQLModel):
    name: Optional[str] = None
    surface: Optional[str] = None
    capacity: Optional[int] = None
    price_per_hour: Optional[float] = None
    is_covered: Optional[bool] = None
    available: Optional[bool] = None

