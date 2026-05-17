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
