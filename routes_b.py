from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from database import get_session
from models_b import Rezervacija, RezervacijaCreate, RezervacijaUpdate

router = APIRouter()

@router.get("/rezervacije")
def get_all_rezervacije(
    status: Optional[str] = None,
    session: Session = Depends(get_session)):

    query = select(Rezervacija)
    if status is not None:
        query = query.where(Rezervacija.status == status)
    return session.exec(query).all()

@router.get("/rezervacije/{id}")
def get_rezervacija(id: int, session: Session = Depends(get_session)):
    rezervacija = session.get(Rezervacija, id)

    if not rezervacija:
        raise HTTPException(status_code=404, detail="Rezervacija nije pronađena")

    return rezervacija

@router.post("/rezervacije", status_code=201)
def create_rezervacija(
    rezervacija_data: RezervacijaCreate,
    session: Session = Depends(get_session)):

    nova_rezervacija = Rezervacija.from_orm(rezervacija_data)

    session.add(nova_rezervacija)
    session.commit()
    session.refresh(nova_rezervacija)

    return nova_rezervacija

@router.put("/rezervacije/{id}")
def update_rezervacija(
    id: int,
    rezervacija_data: RezervacijaCreate,
    session: Session = Depends(get_session)
):
    rezervacija = session.get(Rezervacija, id)

    if not rezervacija:
        raise HTTPException(status_code=404, detail="Rezervacija nije pronađena")

    for key, value in rezervacija_data.dict().items():
        setattr(rezervacija, key, value)

    session.commit()
    session.refresh(rezervacija)

    return rezervacija

@router.patch("/rezervacije/{id}")
def partial_update_rezervacija(
    id: int,
    rezervacija_data: RezervacijaUpdate,
    session: Session = Depends(get_session)
):
    rezervacija = session.get(Rezervacija, id)

    if not rezervacija:
        raise HTTPException(status_code=404, detail="Rezervacija nije pronađena")

    for key, value in rezervacija_data.dict(exclude_unset=True).items():
        setattr(rezervacija, key, value)

    session.commit()
    session.refresh(rezervacija)

    return rezervacija

@router.delete("/rezervacije/{id}", status_code=204)
def delete_rezervacija(id: int, session: Session = Depends(get_session)):
    rezervacija = session.get(Rezervacija, id)

    if not rezervacija:
        raise HTTPException(status_code=404, detail="Rezervacija nije pronađena")

    session.delete(rezervacija)
    session.commit()

    return