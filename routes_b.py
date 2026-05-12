from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from database import get_session
from models_b import Rezervacija,RezervacijaCreate, RezervacijaUpdate


router = APIRouter(prefix="/resursi_b", tags=["Rezervacije"])


@router.post("/rezervacije", response_model=Rezervacija)
def create_rezervacija(
    data: RezervacijaCreate,
    session: Session = Depends(get_session)
):
    rezervacija = Rezervacija.from_orm(data)
    session.add(rezervacija)
    session.commit()
    session.refresh(rezervacija)
    return rezervacija



@router.get("/rezervacije", response_model=list[Rezervacija])
def get_rezervacije(
    status: str | None = None,
    teren_id: int | None = None,
    session: Session = Depends(get_session)
):
    query = select(Rezervacija)

    if status:
        query = query.where(Rezervacija.status == status)

    if teren_id:
        query = query.where(Rezervacija.teren_id == teren_id)

    return session.exec(query).all()


@router.get("/rezervacije/{id}", response_model=Rezervacija)
def get_rezervacija(id: int, session: Session = Depends(get_session)):
    rezervacija = session.get(Rezervacija, id)

    if not rezervacija:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rezervacija nije pronađena"
        )

    return rezervacija










@router.put("/rezervacije/{id}", response_model=Rezervacija)
def update_rezervacija(
    id: int,
    data: RezervacijaUpdate,
    session: Session = Depends(get_session)
):
    rezervacija = session.get(Rezervacija, id)
    if not rezervacija:
        raise HTTPException(status_code=404, detail="Ne postoji")

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(rezervacija, key, value)

    session.add(rezervacija)
    session.commit()
    session.refresh(rezervacija)

    return rezervacija



@router.delete("/rezervacije/{id}")
def delete_rezervacija(id: int, session: Session = Depends(get_session)):
    rezervacija = session.get(Rezervacija, id)
    if not rezervacija:
        raise HTTPException(status_code=404, detail="Ne postoji")

    session.delete(rezervacija)
    session.commit()

    return {"message": "Obrisano"}