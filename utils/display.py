def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title}")
    print("=" * 40)

def print_book_list(books): #show all books in the list
    if not books:
        print("(no books to show)")
        return
    for book in books: #print each book one by one
        print(f"{book}")