import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from ..database import Base
import enum


class OfferStatus(enum.Enum):
    ACTIVE = "active"  # активные
    THINKING = "thinking"  # надо подумать
    BOUGHT = "bought"  # выкупленные


class Offer(Base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    number = Column(Integer)
    price = Column(Float)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    image_url = Column(String)
    status = Column(Enum(OfferStatus, native_enum=False, length=20), default=OfferStatus.ACTIVE, nullable=False)

    buys = relationship("Buy", back_populates="offer")

    def __repr__(self):
        return f"<Offer(id={self.id}, name={self.name}, price={self.price}, status={self.status.value})>"