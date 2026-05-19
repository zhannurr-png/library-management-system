class Book:
    def __init__(self, book_id, title, author, available=True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available

    @property
    def book_id(self):
        return self._book_id
        
    @property
    def id(self):
        return self._book_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise TypeError("Available status must be a boolean")
        self._available = value

    def borrow(self):
        if not self._available:
            raise ValueError(f"Sorry, '{self._title}' is already borrowed.")
        self._available = False

    def return_book(self):
        self._available = True

    def as_tuple(self):
        return (self._book_id, self._title, self._author, self._available)

    def to_dict(self):
        return {"id": self._book_id, "title": self._title, "author": self._author, "available": self._available}

    def __str__(self):
        status = "available" if self._available else "not available"
        return f"[{self._book_id}] {self._title} by {self._author} ({status})"
