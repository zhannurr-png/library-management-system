from services.library_service import LibraryService
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
        print("6. Get book suggestions")
        print("7. Exit")

        choice = safe_int("\nEnter choice: ")

        if choice == 1:
            report_available(service.books)

        elif choice == 2:
            report_borrowed(service.books)

        elif choice == 3:
            print_header("Borrow a book")
            report_available(service.books)
            user_id = safe_int("Enter user ID: ")
            book_id = safe_int("Enter book ID to borrow: ")
            try:
                service.borrow_book(user_id, book_id)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            print_header("Return a book")
            user_id = safe_int("Enter user ID: ")
            book_id = safe_int("Enter book ID to return: ")
            try:
                service.return_book(user_id, book_id)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 5:
            print_header("Borrow history")
            user_id = safe_int("Enter user ID: ")
            if user_id in service.books:
                report_user_history(service.users[user_id], service.transactions)
            else:
                print("User not found")

        elif choice == 6:
            print_header("Book suggestions")
            user_id = safe_int("Enter user ID: ")
            try: #generate suggestions based on borrowing history
                suggestions = service.suggest_book(user_id)
                if suggestions:
                    print("You might like")
                    print_book_list(suggestions)
                else: #no enough data for suggestions
                    print("No suggestions found, borrow more books")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()