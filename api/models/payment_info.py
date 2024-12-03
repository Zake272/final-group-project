from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base

class PaymentInfo(Base):
    __tablename__ = 'payment_info'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    amount_paid = Column(Integer, nullable=False)
    payment_method = Column(String(50), nullable=False)
