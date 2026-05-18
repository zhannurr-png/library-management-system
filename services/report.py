from datetime import date
def report_available(books):
    #show all books that can be borrowed right now
    print("\n--- Available Books ---")
    available = [b for b in books.values() if b.available]
    if not available:
        print("No books currently available.")
    for book in available:
        print(f"  {book}")
    print(f"Total: {len(available)}")
def report_borrowed(books):
    #show all books that are currently borrowed
    print("\n--- Borrowed Books ---")
    borrowed = [b for b in books.values() if not b.available]
    if not borrowed:
        print("No books currently borrowed.")
    for book in borrowed:
        print(f"  {book}")
    print(f"Total: {len(borrowed)}")
def report_user_history(user, transactions):
    # show all borrow and return history for one user
    print(f"\n--- Borrow History for {user.name} ---")
    user_transactions = [t for t in transactions if t.user_id == user.user_id]
    if not user_transactions:
        print("No history found.")
    for t in user_transactions:
        print(f"  {t}")