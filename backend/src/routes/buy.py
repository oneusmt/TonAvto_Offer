from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.buy_service import BuyService
from ..schemas.buy import BuyResponse


router = APIRouter(
    prefix="/api/buy",
    tags=["buy"]
)


@router.get("/buy", response_model=List[BuyResponse], status_code=status.HTTP_200_OK)
def get_buy(db: Session = Depends(get_db)):
    service = BuyService(db)
    return service.get_all_buys()
