from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from database import get_session
from models_a import Teren


router = APIRouter()


@router.get("/tereni")
def get_all_tereni(surface: Optional[str] = None,
                   session: Session = Depends(get_session)):
    query = select(Teren)
    if surface is not None:
        query = query.where(Teren.surface == surface)
    return session.exec(query).all()


@router.get("/tereni/{id}")
def get_teren(id: int, session: Session = Depends(get_session)):
    teren = session.get(Teren, id)
    if not teren:
        raise HTTPException(status_code=404, detail="Teren nije pronađen")
    return teren