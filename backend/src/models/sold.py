from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..database import Base


class Sold(Base):
    __tablename__ = 'sold'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    buy_id = Column(Integer, ForeignKey('buy.id'), nullable=False)
    price = Column(Float)
    profit = Column(Float)

    buy = relationship("Buy", back_populates="solds")

    def __repr__(self):
        return f"<Sold(id={self.id}, name={self.name}, price={self.price}, profit={self.profit})>"