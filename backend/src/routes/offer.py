from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.offer_service import OfferService
from ..schemas.offer import OfferResponse, OfferCreate, OfferUpdate
from ..security import require_token


router = APIRouter(
    prefix="/api/offer",
    tags=["offers"],
    dependencies=[Depends(require_token)],
)


@router.get("", response_model=List[OfferResponse], status_code=status.HTTP_200_OK)
def get_offers(db: Session = Depends(get_db)):
    service = OfferService(db)
    return service.get_all_offers()


@router.post("", response_model=OfferResponse, status_code=status.HTTP_201_CREATED)
def create_offer(offer_data: OfferCreate, db: Session = Depends(get_db)):
    service = OfferService(db)
    return service.create_offer(offer_data)


@router.put("/{offer_id}", response_model=OfferResponse, status_code=status.HTTP_200_OK)
def update_offer(offer_id: int, offer_data: OfferUpdate, db: Session = Depends(get_db)):
    service = OfferService(db)
    return service.update_offer(offer_id, offer_data)


@router.delete("/{offer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    service = OfferService(db)
    service.delete_offer(offer_id)
    return None

