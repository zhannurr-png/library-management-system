from datetime import date
class Transaction:
    def __init__(self, user_id, book_id, action):
        if action not in ("borrow", "return"):
            raise ValueError("Action must be 'borrow' or 'return'")
        self._user_id = user_id
        self._book_id = book_id
        self._action = action
        self._date = date.today().isoformat()

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def action(self):
        return self._action
    
    @property
    def date(self):
        return self._date

        @date.settler
    def date(self, value):
        self._date = value

    def as_tuple(self):     #use tuple to avoid changes in transaction log
        return (self._user_id, self._book_id, self._action, self._date)

    def days_since(self):    #counts how many days ago this transaction happened
        today = date.today()
        transaction_date = date.fromisoformat(self._date)
        diff = today - transaction_date
        return diff.days

    def to_dict(self):
        return {"user_id": self._user_id, "book_id": self._book_id, "action": self._action, "date": self._date}

    def __str__(self):
        return f"[{self._date}] User {self._user_id} did '{self._action}' on book {self._book_id}"
