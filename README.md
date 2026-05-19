# Library Management System

## Project Description
Library Management System is a Python-based console application developed as a final group project for the “Introduction to Programming 2 ” course.

The project simulates a real-world library system where users can borrow and return books, track book availability, manage borrowing history, and receive book recommendations.

The application demonstrates Object-Oriented Programming principles, modular architecture, JSON file handling, testing, and advanced Python concepts.

---

## Features

### Book Management
- Borrow and return books
- Track available and borrowed books
- Prevent borrowing unavailable books
- Prevent duplicate borrowing

### User System
- Member and Admin roles
- Borrowing limit for members
- Unlimited borrowing for admins
- User borrowing history tracking

### Recommendation System
- Book recommendation feature based on similar user borrowing activity
- Uses set intersection for efficient recommendation logic

### Reports
- Available books report
- Borrowed books report
- User borrowing history report

### Data Storage
- JSON-based persistent storage
- Automatic loading and saving of books, users, and transactions

### Python Concepts Used
- Object-Oriented Programming (OOP)
- Inheritance and polymorphism
- Encapsulation with properties and setters
- Generators
- Lambda functions
- Exception handling
- Tuple and dictionary conversion

### Testing
- Automated testing using unittest
- Edge case validation
- Storage and service testing

---

## Technologies Used
- Python 3
- JSON
- unittest
- GitHub

---

## Project Structure

```text
library-management-system/
│
├── data/
│   ├── books.json
│   ├── transactions.json
│   └── users.json
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── transaction.py
│   └── user.py
│
├── services/
│   ├── __init__.py
│   ├── library_service.py
│   ├── report.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_service.py
│   └── tests_storage.py
│
├── utils/
│   ├── __init__.py
│   ├── display.py
│   └── error_handler.py
│
├── .gitignore
├── main.py
└── README.md
```
---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/zhannurr-png/library-management-system.git
```

### 2. Open the project folder

```bash
cd library-management-system
```

### 3. Run the application

```bash
python main.py
```

---

## Example Usage

```text
What would you like to do?

1. Show available books
2. Show borrowed books
3. Borrow a book
4. Return a book
5. Show my history
6. Get book suggestions
7. Exit
```

### Example

```text
Enter choice: 3
Enter user ID: 1
Enter book ID to borrow: 4

Alice successfully borrowed book!
```

---

## Project members
- Assel Yermekkyzy
- Balnur Oraztay
- Aiym Issabayeva
- Zhannur Bakyt