# models.py
# --- ----
# SQLAlchemy ORM models

from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    year = Column(Integer, nullable=True)

    # --- ----
    # Debug helper
    def __repr__(self):
        return f"<Book id={self.id} title={self.title!r}>"
