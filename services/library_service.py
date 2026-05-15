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