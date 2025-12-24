import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Offer(Base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    number = Column(Integer)
    price = Column(Float)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    image_url = Column(String)

    buy = relationship("Buy", back_populates="offers")

    def __repr__(self):
        return f"<Offer(id={self.id}, name={self.name}, price={self.price})>"