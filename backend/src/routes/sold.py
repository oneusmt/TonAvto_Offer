from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.sold_service import SoldService
from ..schemas.sold import SoldResponse, SoldCreate, SoldUpdate


router = APIRouter(
    prefix="/api/sold",
    tags=["sold"]
)


@router.get("", response_model=List[SoldResponse], status_code=status.HTTP_200_OK)
def get_all_solds(db: Session = Depends(get_db)):
    service = SoldService(db)
    return service.get_all_solds(db)


@router.post("", response_model=SoldResponse, status_code=status.HTTP_201_CREATED)
def create_sold(sold_data: SoldCreate, db: Session = Depends(get_db)):
    service = SoldService(db)
    return service.create_sold(sold_data)


@router.put("/{sold_id}", response_model=SoldResponse, status_code=status.HTTP_200_OK)
def update_sold(sold_id: int, sold_data: SoldUpdate, db: Session = Depends(get_db)):
    service = SoldService(db)
    return service.update_sold(sold_id, sold_data)


@router.delete("/{sold_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sold(sold_id: int, db: Session = Depends(get_db)):
    service = SoldService(db)
    service.delete_sold(sold_id)
    return None