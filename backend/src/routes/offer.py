from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.offer_service import OfferService
from ..schemas.offer import OfferResponse


router = APIRouter(
    prefix="/api/offer",
    tags=["offers"]
)


@router.get("", response_model=List[OfferResponse], status_code=status.HTTP_200_OK)


def get_offers(db: Session = Depends(get_db)):
    service = OfferService(db)
    return service.get_all_offers()