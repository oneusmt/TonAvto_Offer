from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.offer import Offer
from ..schemas.offer import OfferCreate, OfferUpdate


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_offers (self) -> List[Offer]:
        return self.db.query(Offer).all()

    def get_by_id(self, offer_id: int) -> Optional[Offer]:
        return self.db.query(Offer).filter(Offer.id == offer_id).first()

    def create(self, offer_data: OfferCreate) -> Offer:
        db_offer = Offer(**offer_data.model_dump())
        self.db.add(db_offer)
        self.db.commit()
        self.db.refresh(db_offer)
        return db_offer

    def update(self, offer_id: int, offer_data: OfferUpdate) -> Optional[Offer]:
        db_offer = self.get_by_id(offer_id)
        if not db_offer:
            return None
        
        update_data = offer_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_offer, field, value)
        
        self.db.commit()
        self.db.refresh(db_offer)
        return db_offer

    def delete(self, offer_id: int) -> bool:
        db_offer = self.get_by_id(offer_id)
        if not db_offer:
            return False
        
        self.db.delete(db_offer)
        self.db.commit()
        return True