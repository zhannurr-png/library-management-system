class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if not self.available:
            raise ValueError(f"Sorry, '{self.title}' is already borrowed.")
        self.available = False

    def return_book(self):
        self.available = True

    def as_tuple(self):
        return (self.book_id, self.title, self.author, self.available)

    def to_dict(self):
        return {
            "id": self.book_id, "title": self.title,
            "author": self.author, "available": self.available}

    def __str__(self):
        if self.available:
            status = "available"
        else:
            status = "not available"
        return f"[{self.book_id}] {self.title} by {self.author} ({status})"
