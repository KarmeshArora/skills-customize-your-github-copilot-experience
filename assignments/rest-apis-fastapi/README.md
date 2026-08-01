# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, learning how to define routes, handle request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI App

#### Description
Set up a FastAPI application with a root endpoint and run it locally using Uvicorn.

#### Requirements
Completed program should:

- Import `FastAPI` and create an `app` instance
- Define a `GET /` route that returns a JSON welcome message
- Include a `/health` route that returns `{"status": "ok"}`

### 🛠️ Build a Books CRUD API

#### Description
Implement a simple in-memory books API with endpoints to create, read, update, and delete book records.

#### Requirements
Completed program should:

- Define a `Book` model using Pydantic with fields: `id` (int), `title` (str), `author` (str), and `year` (int)
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return a single book, returning a 404 error if not found
- Implement `POST /books` to add a new book and return it with status code 201
- Implement `DELETE /books/{book_id}` to remove a book by ID

### 🛠️ Add Query Parameters and Filtering

#### Description
Extend the `GET /books` endpoint to support optional query parameters for filtering results.

#### Requirements
Completed program should:

- Accept an optional `author` query parameter to filter books by author name
- Accept an optional `year` query parameter to filter books published in a specific year
- Return an empty list (not an error) when no books match the filters

Example request:
```
GET /books?author=Orwell&year=1949
```

Example response:
```json
[{"id": 1, "title": "1984", "author": "Orwell", "year": 1949}]
```

### 🛠️ Validate Input with Pydantic and Return Proper Errors

#### Description
Add input validation to the `POST /books` endpoint so that bad data is rejected with a helpful error message.

#### Requirements
Completed program should:

- Enforce that `title` and `author` are non-empty strings (minimum length of 1)
- Enforce that `year` is a realistic integer between 1000 and 2100
- Return FastAPI's automatic 422 Unprocessable Entity response when validation fails
- Include at least one example of using `Field(...)` from Pydantic to add constraints
