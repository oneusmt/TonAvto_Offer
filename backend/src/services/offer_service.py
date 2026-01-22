from sqlalchemy.orm import Session
from typing import List

from ..models import Offer
from ..repositories.offer_repository import OfferRepository
from ..schemas.offer import OfferResponse, OfferCreate, OfferUpdate
from fastapi import HTTPException, status


class OfferService:
    def __init__(self, db: Session):
        self.repository = OfferRepository(db)

    def get_all_offers(self) -> List[OfferResponse]:
        offers = self.repository.get_all_offers()
        result = []
        for offer in offers:
            # Преобразуем enum в строку для сериализации
            offer_dict = offer.__dict__.copy()
            if 'status' in offer_dict and hasattr(offer_dict['status'], 'value'):
                offer_dict['status'] = offer_dict['status'].value
            # Удаляем служебные поля SQLAlchemy
            offer_dict = {k: v for k, v in offer_dict.items() if not k.startswith('_')}
            result.append(OfferResponse.model_validate(offer_dict))
        return result

    def get_offer_by_id(self, offer_id: int) -> OfferResponse:
        offer = self.repository.get_by_id(offer_id)
        if not offer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Offer with id {offer_id} not found"
            )
        offer_dict = offer.__dict__.copy()
        if 'status' in offer_dict and hasattr(offer_dict['status'], 'value'):
            offer_dict['status'] = offer_dict['status'].value
        offer_dict = {k: v for k, v in offer_dict.items() if not k.startswith('_')}
        return OfferResponse.model_validate(offer_dict)

    def create_offer(self, offer_data: OfferCreate) -> OfferResponse:
        offer = self.repository.create(offer_data)
        offer_dict = offer.__dict__.copy()
        if 'status' in offer_dict and hasattr(offer_dict['status'], 'value'):
            offer_dict['status'] = offer_dict['status'].value
        offer_dict = {k: v for k, v in offer_dict.items() if not k.startswith('_')}
        return OfferResponse.model_validate(offer_dict)

    def update_offer(self, offer_id: int, offer_data: OfferUpdate) -> OfferResponse:
        offer = self.repository.update(offer_id, offer_data)
        if not offer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Offer with id {offer_id} not found"
            )
        offer_dict = offer.__dict__.copy()
        if 'status' in offer_dict and hasattr(offer_dict['status'], 'value'):
            offer_dict['status'] = offer_dict['status'].value
        offer_dict = {k: v for k, v in offer_dict.items() if not k.startswith('_')}
        return OfferResponse.model_validate(offer_dict)

    def delete_offer(self, offer_id: int) -> None:
        success = self.repository.delete(offer_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Offer with id {offer_id} not found"
            )