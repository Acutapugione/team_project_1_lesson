from pydantic import BaseModel

class Film(BaseModel):
    id: int
    name: str
    description: str
    rating: float
    genre: str
    actors: list[str]
    poster: str