from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
