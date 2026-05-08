from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import Optional
from database import get_session
from models_a import Teren, TerenCreate, TerenUpdate


router = APIRouter(prefix="/tereni", tags=["Tereni"])


@router.get("/", response_model=list[Teren])
def get_tereni(
    surface: Optional[str] = Query(default=None, description="Filter po vrsti podloge"),
    session: Session = Depends(get_session)
):
    query = select(Teren)
    if surface is not None:
        query = query.where(Teren.surface == surface)
    tereni = session.exec(query).all()
    return tereni


@router.get("/{teren_id}", response_model=Teren)
def get_teren(teren_id: int, session: Session = Depends(get_session)):
    teren = session.get(Teren, teren_id)
    if not teren:
        raise HTTPException(status_code=404, detail="Teren nije pronađen")
    return teren