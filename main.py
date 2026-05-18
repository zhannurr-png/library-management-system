from services.library_service import LibraryService, return_book
from services.report import (report_available, report_borrowed,
    report_user_history)
from utils.display import print_header, print_book_list, print_user_info
from utils.error_handler import safe_int

def main():
    print_header("Welcome to the Library System")
    service = LibraryService()

    while True:
        print("\nWhat would you like to do?")
        print("1. Show available books")
        print("2. Show borrowed books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Show my history")
        print("6. Show overdue books")
        print("7. Get book suggestions")
        print("8. Backup data")
        print("9. Exit")

        choice = safe_int("\nEnter choice: ")

        if choice == 1:
            report_available(service.books)

        elif choice == 2:
            report_borrowed(service.books)

        elif choice == 3:
            print_header("Borrow a book")
            report_available(service.books)
            user_id = safe_int(input("Enter user ID: "))
            book_id = safe_int(input("Enter book ID to borrow: "))
            try:
                service.borrow_book(user_id, book_id)
            except ValueError as e:
                print(f"Error: {e}")