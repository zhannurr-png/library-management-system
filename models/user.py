class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  

    def can_borrow(self):
        raise NotImplementedError("Subclass (Member or Admin) must implement can_borrow()")

    def add_borrowed(self, book_id):
        self.borrowed_books.append(book_id)

    def remove_borrowed(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "borrowed_books": self.borrowed_books}

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id}), borrowed: {self.borrowed_books}"


class Member(User):
    max_borrow = 3      #maximum number of book that can be borrowed

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_borrow

    def __str__(self):
        return f"Member: {self.name} (ID: {self.user_id}), borrowed: {self.borrowed_books}"


class Admin(User):
    def can_borrow(self):
        return True  # admin has no limit

    def __str__(self):
        return f"Admin: {self.name} (ID: {self.user_id}), borrowed: {self.borrowed_books}"
