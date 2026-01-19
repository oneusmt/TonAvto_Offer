from sqlalchemy.orm import Session
from typing import List

from ..models import Sold
from ..repositories.sold_repository import SoldRepository
from ..repositories.buy_repository import BuyRepository
from ..schemas.sold import SoldResponse, SoldCreate, SoldUpdate
from fastapi import HTTPException, status


class SoldService:
    def __init__(self, db: Session):
        self.sold_repository = SoldRepository(db)
        self.buy_repository = BuyRepository(db)

    def get_all_solds(self, db: Session) -> List[SoldResponse]:
        solds = self.sold_repository.get_all_solds()
        return [SoldResponse.model_validate(sold) for sold in solds]

    def get_sold_by_id(self, sold_id: int) -> SoldResponse:
        sold = self.sold_repository.get_by_id(sold_id)
        if not sold:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sold with id {sold_id} not found"
            )
        return SoldResponse.model_validate(sold)

    def create_sold(self, sold_data: SoldCreate) -> SoldResponse:
        sold = self.sold_repository.create(sold_data)
        return SoldResponse.model_validate(sold)

    def update_sold(self, sold_id: int, sold_data: SoldUpdate) -> SoldResponse:
        sold = self.sold_repository.update(sold_id, sold_data)
        if not sold:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sold with id {sold_id} not found"
            )
        return SoldResponse.model_validate(sold)

    def delete_sold(self, sold_id: int) -> None:
        success = self.sold_repository.delete(sold_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sold with id {sold_id} not found"
            )