from pydantic import BaseModel, HttpUrl


class Card(BaseModel):
    """
    Each card represent a single company.
    """
    name: str
    location: list
    stack: list
    flavor: str
    link: HttpUrl
    tags: list
    alt_link: HttpUrl
