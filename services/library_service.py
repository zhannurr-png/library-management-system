from models.book import Book
from models.user import User
from services.storage import(
     load_books, save_books,
     load_users, save_users,
     load_transactions, save_transactions,
)
from models.transaction import Transaction

class LibraryService:
    def __init__(self):
        self.books = load_books()
        self.users = load_users()
        self.transactions = load_transactions()

def borrow_book(self, user_id, book_id):
    if user_id not in self.users:
        raise ValueError("Invalid user_id.")
    if book_id not in self.books:
        raise ValueError("Invalid book_id.")

    user = self.users[user_id]
    book = self.books[book_id]

    if not book.available:
        raise ValueError(f"'{book.title}' is not available right now.")
    if not user.can_borrow():
        raise ValueError(f"'{user.name}' has reached the borrowing limit.")
    if book_id in user.borrowed_books:
        raise ValueError("You already borrowed this book")

    book.borrow()
    user.add_borrowed_book(book_id)

    t = Transaction(user_id, book_id, "borrow")
    self.transactions.append(t)

    save_books(self.books)
    save_users(self.users)
    save_transactions(self.transactions)

    print(f" {user.name} successfully borrowed book! '{book.title}'.")
def return_book(self, user_id, book_id):
    if user_id not in self.users:
        raise ValueError("Invalid user_id.")
    if book_id not in self.books:
        raise ValueError("Invalid book_id.")
    user = self.users[user_id]
    book = self.books[book_id]

    if book_id not in user.borrowed_books:
        raise ValueError("This user didn't borrow this book.")
    book.return_book()
    user.remove_borrowed(book_id)
    t = Transaction(user_id, book_id, "return")
    self.transactions.append(t)

    save_books(self.books)
    save_users(self.users)
    save_transactions(self.transactions)
    print(f" {user.name} successfully returned '{book.title}'.Thank you!")