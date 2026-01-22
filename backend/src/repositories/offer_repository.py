from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.offer import Offer, OfferStatus
from ..schemas.offer import OfferCreate, OfferUpdate


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_offers (self) -> List[Offer]:
        return self.db.query(Offer).all()

    def get_by_id(self, offer_id: int) -> Optional[Offer]:
        return self.db.query(Offer).filter(Offer.id == offer_id).first()

    def create(self, offer_data: OfferCreate) -> Offer:
        data = offer_data.model_dump()
        # Преобразуем строку статуса в enum
        if 'status' in data and isinstance(data['status'], str):
            try:
                # Пробуем найти enum по значению (active, thinking, bought)
                status_value = data['status'].lower()
                for status_enum in OfferStatus:
                    if status_enum.value == status_value:
                        data['status'] = status_enum
                        break
                else:
                    # Если не нашли, используем ACTIVE по умолчанию
                    data['status'] = OfferStatus.ACTIVE
            except (ValueError, AttributeError):
                data['status'] = OfferStatus.ACTIVE
        db_offer = Offer(**data)
        self.db.add(db_offer)
        self.db.commit()
        self.db.refresh(db_offer)
        return db_offer

    def update(self, offer_id: int, offer_data: OfferUpdate) -> Optional[Offer]:
        db_offer = self.get_by_id(offer_id)
        if not db_offer:
            return None
        
        update_data = offer_data.model_dump(exclude_unset=True)
        # Преобразуем строку статуса в enum
        if 'status' in update_data and isinstance(update_data['status'], str):
            try:
                # Пробуем найти enum по значению (active, thinking, bought)
                status_value = update_data['status'].lower()
                for status_enum in OfferStatus:
                    if status_enum.value == status_value:
                        update_data['status'] = status_enum
                        break
                else:
                    # Если не нашли, оставляем текущий статус
                    del update_data['status']
            except (ValueError, AttributeError):
                # Если ошибка, оставляем текущий статус
                if 'status' in update_data:
                    del update_data['status']
        
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