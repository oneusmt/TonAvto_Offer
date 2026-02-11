from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.buy_service import BuyService
from ..schemas.buy import BuyResponse, BuyCreate, BuyUpdate
from ..security import require_token


router = APIRouter(
    prefix="/api/buy",
    tags=["buy"],
    dependencies=[Depends(require_token)],
)


@router.get("", response_model=List[BuyResponse], status_code=status.HTTP_200_OK)
def get_all_buys(db: Session = Depends(get_db)):
    service = BuyService(db)
    return service.get_all_buys(db)


@router.post("", response_model=BuyResponse, status_code=status.HTTP_201_CREATED)
def create_buy(buy_data: BuyCreate, db: Session = Depends(get_db)):
    service = BuyService(db)
    return service.create_buy(buy_data)


@router.put("/{buy_id}", response_model=BuyResponse, status_code=status.HTTP_200_OK)
def update_buy(buy_id: int, buy_data: BuyUpdate, db: Session = Depends(get_db)):
    service = BuyService(db)
    return service.update_buy(buy_id, buy_data)


@router.delete("/{buy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_buy(buy_id: int, db: Session = Depends(get_db)):
    service = BuyService(db)
    service.delete_buy(buy_id)
    return None

