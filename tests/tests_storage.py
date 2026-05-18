import unittest
import json
import os
from services import storage

class TestStorage(unittest.TestCase):

    def test_load_books_returns_dict(self):
        books = storage.load_books()
        self.assertIsInstance(books, dict)  # should return dict, not list

    def test_books_have_correct_keys(self):
        books = storage.load_books()
        for book_id, book in books.items():
            self.assertEqual(book_id, book.id)  # key must match the book's id

    def test_load_users_returns_dict(self):
        users = storage.load_users()
        self.assertIsInstance(users, dict)  # same as books, dict for fast lookup

    def test_stream_books_is_generator(self):
        import types
        books = storage.load_books()
        gen = storage.stream_books(books)
        self.assertIsInstance(gen, types.GeneratorType)  # must be a generator, not a list

    def test_save_and_reload_books(self):
        books = storage.load_books()
        storage.save_books(books)
        reloaded = storage.load_books()
        self.assertEqual(len(books), len(reloaded))  # no books lost after saving

if __name__ == "__main__":
    unittest.main()