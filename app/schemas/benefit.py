from pydantic import BaseModel
from typing import List


class BenefitBase(BaseModel):
    title: str
    description: str


class BenefitSchema(BaseModel):
    createdAt: str
    title: str
    description: str
    benefits: List[BenefitBase]
    id: str
