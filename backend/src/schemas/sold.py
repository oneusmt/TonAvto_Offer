from typing import Optional
from pydantic import BaseModel, Field


class SoldBase(BaseModel):
    name: str = Field(..., description="Name of the Sold")
    buy_id: float = Field(..., description="ID of the Buy")
    price: float = Field(..., description="Price of the Sold")


class SoldCreate(SoldBase):
    pass


class SoldResponse(SoldBase):
    id: int = Field(..., description="ID of the Sold")

    class Config:
        from_attributes = True