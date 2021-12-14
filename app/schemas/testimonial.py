from pydantic import BaseModel
from typing import List


class TestimonialBase(BaseModel):
    createdAt: str
    name: str
    avatar: str
    quote: str
    rating: int
    id: str


class TestimonialSchema(BaseModel):
    createdAt: str
    title: str
    description: str
    testimonials: List[TestimonialBase]
