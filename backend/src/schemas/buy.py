from typing import Optional
from pydantic import BaseModel, Field


class BuyBase(BaseModel):
    name: str = Field(..., description="Name of the Buy")
    offer_id: int = Field(..., description="ID of the Offer")
    price: float = Field(..., description="Price of the Buy")
    vlozheno: int = Field(default=0, description="Вложено (целое число)")


class BuyCreate(BuyBase):
    pass


class BuyUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the Buy")
    offer_id: Optional[int] = Field(None, description="ID of the Offer")
    price: Optional[float] = Field(None, description="Price of the Buy")
    vlozheno: Optional[int] = Field(None, description="Вложено (целое число)")


class BuyResponse(BuyBase):
    id: int = Field(..., description="ID of the Buy")

    class Config:
        from_attributes = True