import unittest
from services.library_service import LibraryService

class TestLibraryService(unittest.TestCase):

    def setUp(self):
        # runs before every test
        self.service = LibraryService()

    def test_get_available_books_returns_list(self):
        result = self.service.get_available_books()
        self.assertIsInstance(result, list)

    def test_all_available_books_are_really_available(self):
        result = self.service.get_available_books()
        for book in result:
            self.assertTrue(book.available)

    def test_borrow_unavailable_book_raises(self):
        with self.assertRaises(ValueError):
            self.service.borrow_book(3, 2)

    def test_user_not_found_raises(self):
        with self.assertRaises(ValueError):
            self.service.borrow_book(999, 1)

    def test_return_book_not_borrowed_raises(self):
        with self.assertRaises(ValueError):
            self.service.return_book(1, 1)

    def test_suggest_books_returns_list(self):
        result = self.service.suggest_book(1)
        self.assertIsInstance(result, list)

    def test_suggest_books_invalid_user_raises(self):
        with self.assertRaises(ValueError):
            self.service.suggest_book(999)

if __name__ == "__main__":
    unittest.main()