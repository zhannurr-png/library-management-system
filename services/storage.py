import json
import os
from models.book import Book
from models.user import Member, Admin
from models.transaction import Transaction

BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
TRANSACTIONS_FILE = "data/transactions.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return {}  # no file yet, nothing to load
    with open(BOOKS_FILE, "r") as f:
        data = json.load(f)
    books = {}
    for item in data:
        b = Book(item["id"], item["title"], item["author"], item["available"])
        books[b.id] = b  # dict so we can find books by id fast
    return books

def save_books(books):
    data = [b.to_dict() for b in books.values()]  # objects -> dicts for json
    with open(BOOKS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}  # file doesn't exist on first run
    with open(USERS_FILE, "r") as f:
        data = json.load(f)
    users = {}
    for item in data:
        if item["user_id"] == 99:
            u = Admin(item["user_id"], item["name"])  # we decided 99 = admin
        else:
            u = Member(item["user_id"], item["name"])
        for book_id in item["borrowed_books"]:
            u.add_borrowed(book_id)  # put their books back
        users[u.user_id] = u
    return users

def save_users(users):
    data = [u.to_dict() for u in users.values()]  # can't write objects to json directly
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        return []  # no file yet, nothing to load
    with open(TRANSACTIONS_FILE, "r") as f:
        data = json.load(f)
    transactions = []
    for item in data:
        t = Transaction(item["user_id"], item["book_id"], item["action"])
        t.date = item["date"]  # keep original date, not today
        transactions.append(t)
    return transactions

def save_transactions(transactions):
    data = [t.to_dict() for t in transactions]  # objects -> dicts for json
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def stream_books(books):
    # yields one book at a time,no need to load all into memory
    for book in books.values():
        yield book