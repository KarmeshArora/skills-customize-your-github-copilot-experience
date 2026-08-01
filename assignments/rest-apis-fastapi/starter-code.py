from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Books API")

# --- Task 1: Basic App Setup ---
# TODO: Add a GET "/" route that returns a welcome message
# TODO: Add a GET "/health" route that returns {"status": "ok"}


# --- Task 2: Books CRUD API ---
# Pydantic model for a Book
class Book(BaseModel):
    id: int
    # TODO: Add title, author, and year fields


# In-memory store
books: list[Book] = []

# TODO: Implement GET /books - return all books
# TODO: Implement GET /books/{book_id} - return one book or 404
# TODO: Implement POST /books - add a new book, return 201
# TODO: Implement DELETE /books/{book_id} - remove a book by ID


# --- Task 3: Query Parameters and Filtering ---
# TODO: Update GET /books to accept optional `author` and `year` query parameters
# Example: GET /books?author=Orwell&year=1949


# --- Task 4: Pydantic Validation ---
# TODO: Update the Book model to use Field(...) to enforce:
#   - title and author have a minimum length of 1
#   - year is between 1000 and 2100
# Example:
#   title: str = Field(..., min_length=1)
#   year: int = Field(..., ge=1000, le=2100)
