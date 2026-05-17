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