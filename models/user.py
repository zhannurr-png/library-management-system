class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  

    def can_borrow(self):
        return False    

    def add_borrowed(self, book_id):
        self.borrowed_books.append(book_id)

    def remove_borrowed(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "borrowed_books": self.borrowed_books}

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id}), borrowed: {self.borrowed_books}"
