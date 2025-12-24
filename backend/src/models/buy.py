from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Buy(Base):
    __tablename__ = "buy"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    offer = relationship("Offer", back_populates="buy")

    def __repr__(self):
        return f"<Buy(id={self.id}, name={self.name}, price={self.price})>"