from typing import Optional
from pydantic import BaseModel
from .resources import Resource

class OrderDetailBase(BaseModel):
    amount: int

class OrderDetailCreate(OrderDetailBase):
    order_id: int
    resource_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    resource: Resource = None

    class Config:
        from_attributes = True