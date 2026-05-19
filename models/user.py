class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._borrowed_books = []  

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def borrowed_books(self):
        return self._borrowed_books.copy()
    
    def can_borrow(self):
        raise NotImplementedError("Subclass (Member or Admin) must implement can_borrow()") 
    
    def add_borrowed(self, book_id):
        if book_id not in self._borrowed_books:
            self._borrowed_books.append(book_id)
    
    def remove_borrowed(self, book_id):
        if book_id in self._borrowed_books:
            self._borrowed_books.remove(book_id)

    def to_dict(self):
        return {"user_id": self._user_id, "name": self._name, "borrowed_books": self._borrowed_books.copy()}

    def __str__(self):
        return f"User: {self._name} (ID: {self._user_id}), borrowed: {self._borrowed_books}"

class Member(User):
    max_borrow = 3     #maximum number of book that can be borrowed

    def can_borrow(self):
        return len(self._borrowed_books) < self.max_borrow

    def __str__(self):
        return f"Member: {self._name} (ID: {self._user_id}), borrowed: {self._borrowed_books}"

class Admin(User):
    def can_borrow(self):
        return True   # admin has no limit

    def __str__(self):
        return f"Admin: {self._name} (ID: {self._user_id}), borrowed: {self._borrowed_books}"
