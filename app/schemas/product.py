from pydantic import BaseModel


class ProductSchema(BaseModel):
    createdAt: str
    name: str
    price: str
    image: str
    id: str
