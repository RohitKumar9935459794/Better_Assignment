# Better_Intern_Assignment

## Description
This project is a simple **Better_Intern_Assignment** implemented using Flask. It allows users to perform CRUD operations (Create, Read, Update, Delete) on books. The API is secured using token-based authentication and includes search functionality and pagination.

---

## Features
1. **CRUD Operations for Books**
    - Create a new book.
    - Retrieve all books (with optional search and pagination).
    - Update book details by ID.
    - Delete a book by ID.

2. **Search Functionality**
    - Search books by title and/or author.

3. **Pagination**
    - Paginated responses to retrieve books in chunks.

4. **Token-Based Authentication**
    - Secures API endpoints using a simple Bearer token.

---

## How to Run the Project

### Prerequisites
- Python 3.7 or later

### Steps
1. **Clone the Repository**:
    ```
    git clone https://github.com/RohitKumar9935459794/Better_Assignment
    cd Better_Assignment
    ```

2. **Set Up a Virtual Environment**:
    ```
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. **Install Required Dependencies**:
    ```
    pip install flask
    ```

4. **Set Up the Database**:
    - The database will be automatically created when the application is run for the first time.

5. **Run the Flask Application**:
    ``
    python app.py
    ```

6. **Access the API**:
    The API will be available at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. Create a Book
- **URL**: `/books`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
    ```json
    {
        "title": "Flask in Action",
        "author": "John Doe",
        "isbn": "123456789",
        "published_year": 2023
    }
    ```
- **Response**:
    ```json
    {
        "message": "Book created successfully"
    }
    ```

### 2. Retrieve All Books
- **URL**: `/books`
- **Method**: `GET`
- **Authentication**: Required
- **Query Parameters**:
    - `title` (optional): Filter by title.
    - `author` (optional): Filter by author.
    - `page` (optional): Pagination, defaults to 1.
    - `per_page` (optional): Items per page, defaults to 10.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "title": "Flask in Action",
            "author": "John Doe",
            "isbn": "123456789",
            "published_year": 2023
        }
    ]
    ```

### 3. Update a Book
- **URL**: `/books/<id>`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**:
    ```json
    {
        "title": "Flask Updated",
        "author": "Jane Smith",
        "isbn": "987654321",
        "published_year": 2024
    }
    ```
- **Response**:
    ```json
    {
        "message": "Book updated successfully"
    }
    ```

### 4. Delete a Book
- **URL**: `/books/<id>`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**:
    ```json
    {
        "message": "Book deleted successfully"
    }
    ```

### 5. Search for Books
- **URL**: `/books`
- **Method**: `GET`
- **Authentication**: Required
- **Query Parameters**:
    - `title`: Search by title (partial matches allowed).
    - `author`: Search by author (partial matches allowed).

---

## Authentication
- The API uses token-based authentication.
- All requests to secured endpoints must include the following header:
    ```
    Authorization: Bearer secure_token_123
    ```

---

## Database
The application uses SQLite to store book records. The database is automatically created in the `database/library.db` file.

### Schema
- **Table**: `books`
    - `id` (integer, primary key, auto-increment)
    - `title` (text)
    - `author` (text)
    - `isbn` (text)
    - `published_year` (integer)

---

## Testing
### Using Curl
- **Add a Book**:
    ```
    curl -X POST http://127.0.0.1:5000/books \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer secure_token_123" \
    -d '{"title": "Flask in Action", "author": "John Doe", "isbn": "123456789", "published_year": 2023}'
    ```
- **Retrieve Books**:
    ```
    curl -X GET "http://127.0.0.1:5000/books?title=Flask" \
    -H "Authorization: Bearer secure_token_123"
    ```
- **Update a Book**:
    ```
    curl -X PUT http://127.0.0.1:5000/books/1 \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer secure_token_123" \
    -d '{"title": "Flask Updated", "author": "Jane Smith", "isbn": "987654321", "published_year": 2024}'
    ```
- **Delete a Book**:
    ```
    curl -X DELETE http://127.0.0.1:5000/books/1 \
    -H "Authorization: Bearer secure_token_123"
    ```

### Automated Testing
- Run the tests using:
    ```
    python tests.py
    ```
- The tests will validate all CRUD operations and authentication.

---

## Design Choices
1. **SQLite**: Chosen for simplicity and portability.
2. **Token Authentication**: Ensures only authorized users can access the API.
3. **Pagination**: Handles large datasets efficiently.
4. **Flask Blueprints**: Modularizes the application for scalability.

---

## Assumptions and Limitations
1. Authentication uses a static token (`secure_token_123`) for simplicity. No user management is implemented.
2. No advanced validation for ISBN or published year.
3. Database schema is minimal and may need to be extended for real-world applications.
4. No frontend integration is provided in this project.

---

## Conclusion
This project implements a basic Library Management System with a RESTful API. It showcases core Flask functionality, database integration, and secure API development. The project is extensible and can serve as a foundation for more complex applications.

