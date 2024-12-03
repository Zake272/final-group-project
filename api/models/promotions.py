from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True)
    promo_code = Column(String(50), nullable=False)
    discount_percentage = Column(Integer, nullable=False)
    description = Column(String(255))
