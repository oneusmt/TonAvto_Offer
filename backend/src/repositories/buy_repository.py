from sqlalchemy.orm import Session, joinedload
from typing import Optional, List
from ..models.buy import Buy
from ..schemas.buy import BuyCreate


class BuyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Buy]:
        return self.db.query(Buy).options(joinedload(Buy.offers)).all()

    def create(self, buy_data: BuyCreate) -> Buy:
        db_buy = Buy(**buy_data.model_dump())
        self.db.add(db_buy)
        self.db.commit()
        self.db.refresh(db_buy)
        return db_buy