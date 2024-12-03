from pydantic import BaseModel

class Promotion(BaseModel):
    id: int
    promo_code: str
    discount_percentage: int
    description: str | None

    class Config:
        orm_mode = True
