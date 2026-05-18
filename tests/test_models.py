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


class TestUser(unittest.TestCase):

    def test_member_limit(self):
        m = Member(1, "Alice")
        m.add_borrowed(1)
        m.add_borrowed(2)
        m.add_borrowed(3)
        self.assertFalse(m.can_borrow())  #since reached limit

    def test_member_can_borrow(self):
        m = Member(1, "Alice")
        m.add_borrowed(1)
        self.assertTrue(m.can_borrow())  #only 1 book is borowed,max limit is 3

    def test_admin_no_limit(self):
        a = Admin(2, "Bob")
        for i in range(20):
            a.add_borrowed(i)
        self.assertTrue(a.can_borrow())  #always true for admin

    def test_remove_borrowed(self):
        m = Member(1, "Alice")
        m.add_borrowed(1)
        m.remove_borrowed(1)
        self.assertNotIn(1, m.borrowed_books)
class TestTransaction(unittest.TestCase):

    def test_wrong_action(self):
        with self.assertRaises(ValueError):
            Transaction(1, 1, "delete")

    def test_as_tuple_has_4_items(self):
        t = Transaction(1, 2, "borrow")
        self.assertEqual(len(t.as_tuple()), 4)

    def test_days_since_is_zero_today(self):
        t = Transaction(1, 2, "borrow")
        self.assertEqual(t.days_since(), 0) 

    def test_to_dict(self):
        t = Transaction(1, 2, "borrow")
        d = t.to_dict()
        self.assertEqual(d["user_id"], 1)
        self.assertEqual(d["book_id"], 2)
        self.assertEqual(d["action"], "borrow")

if __name__ == "__main__":
    unittest.main()
