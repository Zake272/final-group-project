from pydantic import BaseModel

class PaymentInfo(BaseModel):
    id: int
    order_id: int
    amount_paid: int
    payment_method: str

    class Config:
        orm_mode = True
