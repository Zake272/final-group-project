from pydantic import BaseModel

class RatingsReviews(BaseModel):
    id: int
    customer_id: int
    order_id: int
    rating: int
    review: str

    class Config:
        orm_mode = True
