# main.py
# --- ----
# FastAPI application with CRUD endpoints

from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")

@app.post("/books/", response_model=schemas.BookOut)
def create_book_endpoint(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/", response_model=List[schemas.BookOut])
def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.BookOut)
def get_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book_endpoint(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}

@app.get("/books/search/", response_model=List[schemas.BookOut])
def search_books_endpoint(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    return crud.search_books(db, q)
