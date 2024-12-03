from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    description: str | None
    price: int
    category: str

    class Config:
        orm_mode = True
