from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.offer import Offer
from ..schemas.offer import OfferCreate


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all (self) -> List[Offer]:
        return self.db.query(Offer).all()

    def create(self, offer_data: OfferCreate) -> Offer:
        db_offer = Offer(**offer_data.model_dump())
        self.db.add(db_offer)
        self.db.commit()
        self.db.refresh(db_offer)
        return db_offer