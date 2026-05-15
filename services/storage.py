import json
import os
from models.book import Book
from models.user import Member, Admin
from models.transaction import Transaction

BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
TRANSACTIONS_FILE = "data/transactions.json"