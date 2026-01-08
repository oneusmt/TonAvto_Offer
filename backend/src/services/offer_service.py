from sqlalchemy.orm import Session
from typing import List

from ..models import Offer
from ..repositories.offer_repository import OfferRepository
from ..schemas.offer import OfferResponse, OfferCreate
from fastapi import HTTPException, status


class OfferService:
    def __init__(self, db: Session):
        self.repository = OfferRepository(db)

    def get_all_offers(self) -> List[OfferResponse]:
        offers = self.repository.get_all_offers()
        return [OfferResponse.model_validate(off) for off in offers]

    def create_offer(self, offer_data: OfferCreate) -> OfferResponse:
        offer = self.repository.create(offer_data)
        return OfferResponse.model_validate(offer)