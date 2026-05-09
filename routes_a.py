from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from database import get_session
from models_a import Teren, TerenCreate, TerenUpdate


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


@router.post("/tereni", status_code=201)
def create_teren(teren_data: TerenCreate,
                 session: Session = Depends(get_session)):
    novi_teren = Teren.from_orm(teren_data)
    session.add(novi_teren)
    session.commit()
    session.refresh(novi_teren)
    return novi_teren


@router.put("/tereni/{id}")
def update_teren(id: int, teren_data: TerenCreate,
                 session: Session = Depends(get_session)):
    teren = session.get(Teren, id)
    if not teren:
        raise HTTPException(status_code=404, detail="Teren nije pronađen")
    for key, value in teren_data.dict().items():
        setattr(teren, key, value)
    session.commit()
    session.refresh(teren)
    return teren


@router.patch("/tereni/{id}")
def partial_update_teren(id: int, teren_data: TerenUpdate,
                         session: Session = Depends(get_session)):
    teren = session.get(Teren, id)
    if not teren:
        raise HTTPException(status_code=404, detail="Teren nije pronađen")
    for key, value in teren_data.dict(exclude_unset=True).items():
        setattr(teren, key, value)
    session.commit()
    session.refresh(teren)
    return teren


@router.delete("/tereni/{id}", status_code=204)
def delete_teren(id: int, session: Session = Depends(get_session)):
    teren = session.get(Teren, id)
    if not teren:
        raise HTTPException(status_code=404, detail="Teren nije pronađen")
    session.delete(teren)
    session.commit()
    return