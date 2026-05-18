import unittest
from models.book import Book
from models.user import Member, Admin
from models.transaction import Transaction

class TestBook(unittest.TestCase):

    def test_borrow_works(self):
        b = Book(1, "Clean Code", "Martin")
        b.borrow()
        self.assertFalse(b.available)

    def test_borrow_already_borrowed(self):
        b = Book(1, "Clean Code", "Martin", available=False)
        with self.assertRaises(ValueError):
            b.borrow()

    def test_return_book(self):
        b = Book(1, "Clean Code", "Martin", available=False)
        b.return_book()
        self.assertTrue(b.available)

    def test_as_tuple(self):
        b = Book(2, "Python Crash Course", "Matthes")
        t = b.as_tuple()
        self.assertIsInstance(t, tuple)
        self.assertEqual(t[0], 2)
    
    def test_to_dict(self):
        b = Book(1, "Clean Code", "Martin")
        d = b.to_dict()
        self.assertEqual(d["id"], 1)
        self.assertEqual(d["title"], "Clean Code")
        self.assertTrue(d["available"])
