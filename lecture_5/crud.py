# crud.py
# --- ----
# Functions to interact with DB (CRUD)

from sqlalchemy.orm import Session
import models, schemas
from typing import List, Optional

def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate) -> Optional[models.Book]:
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author
    if book.year is not None:
        db_book.year = book.year
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int) -> bool:
    db_book = get_book(db, book_id)
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True

def search_books(db: Session, q: str):
    query = db.query(models.Book).filter(
        (models.Book.title.contains(q)) | (models.Book.author.contains(q))
    )
    if q.isdigit():
        query = query.union(db.query(models.Book).filter(models.Book.year == int(q)))
    return query.all()
