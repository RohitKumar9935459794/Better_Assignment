from flask import Blueprint, request, jsonify
from models import get_db_connection
import datetime

library_routes = Blueprint("library", __name__)

# Hardcoded tokens for simplicity
TOKENS = {"admin": "secure_token_123"}

# Middleware for token-based authentication
def authenticate(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token.split(" ")[1] not in TOKENS.values():
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# CRUD: Create Book
@library_routes.route("/books", methods=["POST"])
@authenticate
def create_book():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    isbn = data.get("isbn")
    published_year = data.get("published_year")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO books (title, author, isbn, published_year) VALUES (?, ?, ?, ?)",
            (title, author, isbn, published_year)
        )
        conn.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
    return jsonify({"message": "Book created successfully"}), 201

# CRUD: Get Books with Pagination and Search
@library_routes.route("/books", methods=["GET"])
@authenticate
def get_books():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    search_title = request.args.get("title", "")
    search_author = request.args.get("author", "")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM books WHERE title LIKE ? AND author LIKE ? LIMIT ? OFFSET ?"
    results = cursor.execute(
        query, (f"%{search_title}%", f"%{search_author}%", per_page, (page - 1) * per_page)
    ).fetchall()
    conn.close()
    
    books = [dict(row) for row in results]
    return jsonify(books), 200

# CRUD: Update Book
@library_routes.route("/books/<int:book_id>", methods=["PUT"])
@authenticate
def update_book(book_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE books SET title = ?, author = ?, isbn = ?, published_year = ? WHERE id = ?",
            (data["title"], data["author"], data["isbn"], data["published_year"], book_id)
        )
        conn.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
    return jsonify({"message": "Book updated successfully"}), 200

# CRUD: Delete Book
@library_routes.route("/books/<int:book_id>", methods=["DELETE"])
@authenticate
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
    finally:
        conn.close()
    return jsonify({"message": "Book deleted successfully"}), 200
