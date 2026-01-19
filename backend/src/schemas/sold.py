from typing import Optional
from pydantic import BaseModel, Field


class SoldBase(BaseModel):
    name: str = Field(..., description="Name of the Sold")
    buy_id: int = Field(..., description="ID of the Buy")
    price: float = Field(..., description="Price of the Sold")


class SoldCreate(SoldBase):
    pass


class SoldUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the Sold")
    buy_id: Optional[int] = Field(None, description="ID of the Buy")
    price: Optional[float] = Field(None, description="Price of the Sold")


class SoldResponse(SoldBase):
    id: int = Field(..., description="ID of the Sold")

    class Config:
        from_attributes = True