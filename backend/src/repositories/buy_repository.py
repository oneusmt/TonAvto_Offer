from sqlalchemy.orm import Session, joinedload
from typing import Optional, List
from ..models.buy import Buy
from ..schemas.buy import BuyCreate, BuyUpdate


class BuyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_buys(self) -> List[Buy]:
        return self.db.query(Buy).all()

    def get_by_id(self, buy_id: int) -> Optional[Buy]:
        return self.db.query(Buy).filter(Buy.id == buy_id).first()

    def create(self, buy_data: BuyCreate) -> Buy:
        db_buy = Buy(**buy_data.model_dump())
        self.db.add(db_buy)
        self.db.commit()
        self.db.refresh(db_buy)
        return db_buy

    def update(self, buy_id: int, buy_data: BuyUpdate) -> Optional[Buy]:
        db_buy = self.get_by_id(buy_id)
        if not db_buy:
            return None
        
        update_data = buy_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_buy, field, value)
        
        self.db.commit()
        self.db.refresh(db_buy)
        return db_buy

    def delete(self, buy_id: int) -> bool:
        db_buy = self.get_by_id(buy_id)
        if not db_buy:
            return False
        
        self.db.delete(db_buy)
        self.db.commit()
        return True