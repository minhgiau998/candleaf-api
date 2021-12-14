from pydantic import BaseModel


class HeroSchema(BaseModel):
    createdAt: str
    title: str
    description: str
    id: str
