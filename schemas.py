# schemas.py

from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str

class Book(BookCreate):
    id: int

    class Config:
        # Change orm_mode to from_attributes for Pydantic V2
        from_attributes = True # CORRECTED LINE HERE
