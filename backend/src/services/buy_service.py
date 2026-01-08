from sqlalchemy.orm import Session
from typing import List

from ..models import Buy
from ..repositories.buy_repository import BuyRepository
from ..repositories.offer_repository import OfferRepository
from ..schemas.buy import BuyResponse, BuyCreate
from fastapi import HTTPException, status


class BuyService:
    def __init__(self, db: Session):
        self.buy_repository = BuyRepository(db)
        self.offer_repository = OfferRepository(db)

    def get_all_buys(self, db: Session) -> List[BuyResponse]:
        buys = self.buy_repository.get_all_buys()
        return [BuyResponse.model_validate(buy) for buy in buys]
        """buys = self.buy_repository.get_all()
        buy_repository = [BuyRepository.model_validate(buy) for buy in buys]
        return BuyResponse(buys=buy_repository)"""



    def create_buy(self, buy_data: BuyCreate) -> BuyResponse:
        buy = self.buy_repository.create(buy_data)
        return BuyResponse(buy)
