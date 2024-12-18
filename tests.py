import unittest
import app

class LibraryAPITest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.headers = {"Authorization": "Bearer secure_token_123"}

    def test_create_book(self):
        response = self.app.post("/books", json={
            "title": "Test Book",
            "author": "Author Name",
            "isbn": "1234567890",
            "published_year": 2024
        }, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get("/books", headers=self.headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
