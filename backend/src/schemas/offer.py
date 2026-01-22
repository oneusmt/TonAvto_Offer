import datetime
from typing import Optional

from pydantic import BaseModel, Field
from ..models.offer import OfferStatus


class OfferBase(BaseModel):
    name: str = Field(..., description="Name of the offer")
    description: Optional[str] = Field(None, description="Description of the offer")
    number: int = Field(..., description="Number of the offer")
    price: float = Field(..., description="Price of the offer")
    """date_created: datetime"""
    image_url: Optional[str] = Field(None, description="Image url of the offer")
    status: str = Field(default="active", description="Status of the offer: active, thinking, bought")


class OfferCreate(OfferBase):
    pass


class OfferUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the offer")
    description: Optional[str] = Field(None, description="Description of the offer")
    number: Optional[int] = Field(None, description="Number of the offer")
    price: Optional[float] = Field(None, description="Price of the offer")
    image_url: Optional[str] = Field(None, description="Image url of the offer")
    status: Optional[str] = Field(None, description="Status of the offer: active, thinking, bought")


class OfferResponse(OfferBase):
    id: int = Field(..., description="ID of the offer")

    class Config:
        from_attributes = True
