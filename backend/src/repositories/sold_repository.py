from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.sold import Sold
from ..schemas.sold import SoldCreate


class SoldRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_solds(self) -> List[Sold]:
        return self.db.query(Sold).all()

    def get_by_id(self, id: int) -> Optional[Sold]:
        return self.db.query(Sold).filter(Sold.id == id).first()

    def create(self, sold_data: SoldCreate) -> Sold:
        db_sold = Sold(**sold_data.model.dump())
        self.db.add(db_sold)
        self.db.commit()
        self.db.refresh(db_sold)
        return db_sold

    def delete(self, sold_id: int) -> bool:
        db_sold = self.get_by_id(sold_id)
        if not db_sold:
            return False

        self.db.delete(db_sold)
        self.db.commit()
        return True

