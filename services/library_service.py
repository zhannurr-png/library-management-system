from models.book import Book
from models.user import User
from services.storage import(
     load_books, save_books,
     load_users, save_users,
     load_transactions, save_transactions,
)
from models.transaction import Transaction

class LibraryService:
    #load everything from files
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
        user.add_borrowed(book_id)

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

        #make sure user actually borrowed this book
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

    def get_available_books(self):
        return list(filter(lambda book: book.available, self.books.values()))
    def get_borrowed_books(self):
        return list(filter(lambda book: not book.available, self.books.values()))
    def get_user_history(self, user_id):
        return [t for t in self.transactions if t.user_id == user_id]
    def suggest_book(self, user_id):
        #extra feature: recommend books based on similiar users
        if user_id not in self.users:
            raise ValueError("Invalid user_id.")

        user = self.users[user_id]
        user_books = set(user.borrowed_books)
        #find users who borrowed at least one same book
        #set intersection is faster than nested loops
        similar_users = [
            user for uid, in self.users.items()
        if uid != user_id and set (user.borrowed_books) & user_books]

        #collect all books similar users borrowed
        suggestions = set()
        for similar in similar_users:
            suggestions |= set(similar.borrowed_books)

        #remove books this user already has
        suggestions -= user_books
        result = [self.books[book_id] for book_id in suggestions if book_id in self.books and self.books[book_id].available]
        return result