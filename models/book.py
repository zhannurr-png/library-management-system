class Book:
    def __init__(self, book_id, title, author, available=True):
        self._id = book_id
        self._title = title
        self._author = author
        self._available = available

    def id(self):
        return self._id

    def title(self):
        return self._title

    def author(self):
        return self._author

    def available(self):
        return self._available
