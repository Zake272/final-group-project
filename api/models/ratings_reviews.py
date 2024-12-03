from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base

class RatingsReviews(Base):
    __tablename__ = 'ratings_reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    rating = Column(Integer, nullable=False)
    review = Column(String(255))
