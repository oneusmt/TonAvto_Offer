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
        # Вычисляем прибыль автоматически, если не указана
        data = sold_data.model_dump()
        if 'profit' not in data or data.get('profit') is None or data.get('profit') == 0:
            buy = self.buy_repository.get_by_id(data['buy_id'])
            if buy:
                # profit = sold.price - buy.price - buy.vlozheno
                data['profit'] = data['price'] - buy.price - (buy.vlozheno or 0)
            else:
                data['profit'] = 0.0
        
        # Создаем объект SoldCreate с вычисленной прибылью
        from ..schemas.sold import SoldCreate
        sold_data_with_profit = SoldCreate(**data)
        sold = self.sold_repository.create(sold_data_with_profit)
        return SoldResponse.model_validate(sold)

    def update_sold(self, sold_id: int, sold_data: SoldUpdate) -> SoldResponse:
        # Если обновляется цена или buy_id, пересчитываем прибыль
        update_data = sold_data.model_dump(exclude_unset=True)
        if 'price' in update_data or 'buy_id' in update_data:
            # Получаем текущую запись
            current_sold = self.sold_repository.get_by_id(sold_id)
            if current_sold:
                # Определяем buy_id (новый или текущий)
                buy_id = update_data.get('buy_id', current_sold.buy_id)
                buy = self.buy_repository.get_by_id(buy_id)
                
                # Определяем цену (новую или текущую)
                price = update_data.get('price', current_sold.price)
                
                if buy:
                    # profit = sold.price - buy.price - buy.vlozheno
                    update_data['profit'] = price - buy.price - (buy.vlozheno or 0)
                else:
                    update_data['profit'] = 0.0
        
        # Создаем объект SoldUpdate с вычисленной прибылью
        from ..schemas.sold import SoldUpdate
        sold_data_with_profit = SoldUpdate(**update_data)
        sold = self.sold_repository.update(sold_id, sold_data_with_profit)
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