class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def id(self):
        return self.book_id

    def title(self):
        return self.title

    def author(self):
        return self.author

    def available(self):
        return self.available
