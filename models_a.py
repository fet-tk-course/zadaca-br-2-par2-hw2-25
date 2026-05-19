from sqlmodel import SQLModel, Field
from typing import Optional

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

class TerenUpdate(SQLModel):
    name: Optional[str] = None
    surface: Optional[str] = None
    capacity: Optional[int] = None
    price_per_hour: Optional[float] = None
    is_covered: Optional[bool] = None
    available: Optional[bool] = None