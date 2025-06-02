# routes/books.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional # Import Optional

from database import get_db
import schemas
import models

router = APIRouter()

@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[schemas.Book])
def get_all_books(
    title: Optional[str] = Query(None, description="Filter by book title (case-insensitive)"),
    author: Optional[str] = Query(None, description="Filter by book author (case-insensitive)"),
    genre: Optional[str] = Query(None, description="Filter by book genre (case-insensitive)"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if genre:
        query = query.filter(models.Book.genre.ilike(f"%{genre}%"))

    books = query.all()

    if not books and (title or author or genre): # If no books found AND search parameters were used
        raise HTTPException(status_code=404, detail="No books found matching the search criteria")
    elif not books: # If no books found AND no search parameters were used (empty library)
        return []

    return books

# You can add other CRUD operations like get_book_by_id, update_book, delete_book here later
