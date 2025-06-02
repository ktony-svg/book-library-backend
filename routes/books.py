# routes/books.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# --- CRITICAL CHANGE: Use ABSOLUTE IMPORTS for modules at the project root ---
# These imports assume that 'database', 'models', and 'schemas'
# are directly accessible at the same level as main.py (the project root).
import database # Import the entire database module
import models   # Import the entire models module
import schemas  # Import the entire schemas module
# --- END CRITICAL CHANGE ---

router = APIRouter()

@router.get("/", response_model=List[schemas.Book])
def get_books(db: Session = Depends(database.get_db)): # Access get_db via database.get_db
    """
    Retrieves a list of all books from the database.
    """
    return db.query(models.Book).all()

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)): # Access get_db via database.get_db
    """
    Creates a new book entry in the database.
    """
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
