from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0')

    resource = relationship("Resource", back_populates="recipes")