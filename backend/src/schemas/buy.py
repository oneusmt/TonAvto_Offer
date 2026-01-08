from pydantic import BaseModel, Field


class BuyBase(BaseModel):
    name: str = Field(..., description="Name of the Buy")
    offer_id: int = Field(..., description="ID of the Offer")
    price: float = Field(..., description="Price of the Buy")


class BuyCreate(BuyBase):
    pass


class BuyResponse(BuyBase):
    id: int = Field(..., description="ID of the Buy")

    class Config:
        from_attributes = True