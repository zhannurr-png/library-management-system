from datetime import date
class Transaction:
    def __init__(self, user_id, book_id, action):
        if action not in ("borrow", "return"):
            raise ValueError("Action must be 'borrow' or 'return'")
        self.user_id = user_id
        self.book_id = book_id
        self.action = action
        self.date = date.today().isoformat()

    def as_tuple(self): #use tuple to avoid changes in transaction log
        return (self.user_id, self.book_id, self.action, self.date)

    def days_since(self): #counts how many days ago this transaction happened
        today = date.today()
        transaction_date = date.fromisoformat(self.date)
        diff = today - transaction_date
        return diff.days

    def to_dict(self):
        return {"user_id": self.user_id, "book_id": self.book_id, "action": self.action, "date": self.date}

    def __str__(self):
        return f"[{self.date}] User {self.user_id} did '{self.action}' on book {self.book_id}"
