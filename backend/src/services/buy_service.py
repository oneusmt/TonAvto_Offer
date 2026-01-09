from sqlalchemy.orm import Session
from typing import List

from ..models import Buy
from ..repositories.buy_repository import BuyRepository
from ..repositories.offer_repository import OfferRepository
from ..schemas.buy import BuyResponse, BuyCreate, BuyUpdate
from fastapi import HTTPException, status


class BuyService:
    def __init__(self, db: Session):
        self.buy_repository = BuyRepository(db)
        self.offer_repository = OfferRepository(db)

    def get_all_buys(self, db: Session) -> List[BuyResponse]:
        buys = self.buy_repository.get_all_buys()
        return [BuyResponse.model_validate(buy) for buy in buys]

    def get_buy_by_id(self, buy_id: int) -> BuyResponse:
        buy = self.buy_repository.get_by_id(buy_id)
        if not buy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Buy with id {buy_id} not found"
            )
        return BuyResponse.model_validate(buy)

    def create_buy(self, buy_data: BuyCreate) -> BuyResponse:
        buy = self.buy_repository.create(buy_data)
        return BuyResponse.model_validate(buy)

    def update_buy(self, buy_id: int, buy_data: BuyUpdate) -> BuyResponse:
        buy = self.buy_repository.update(buy_id, buy_data)
        if not buy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Buy with id {buy_id} not found"
            )
        return BuyResponse.model_validate(buy)

    def delete_buy(self, buy_id: int) -> None:
        success = self.buy_repository.delete(buy_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Buy with id {buy_id} not found"
            )
