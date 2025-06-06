# book-library-backend#   B o o k L i b r a r y A p p 
# book-library-backend

📚 Library App Backend

This is the backend for my Library App project, built using FastAPI and SQLAlchemy. The goal of this backend is to help manage a digital library system by enabling the addition of books, tracking borrowing activity, and maintaining user records. It is designed for easy integration with a frontend.

📌 Project aim

This backend supports the following main features:

Adding new books to the library catalog

Viewing borrowing history by user

Searching for books or users by various fields

🧍 Models & Relationships

📖 Book
id: Integer (Primary key)

title: String

author: String

👤 User

id: Integer (Primary key)

name: String

📅 BorrowRecord

id: Integer

book_id: ForeignKey → Book

user_id: ForeignKey → User

🔗 Relationships

One User ➝ many BorrowRecords

One Book ➝ many BorrowRecords

🧠 User Stories (Backend Support)

✅ I can add a new book to the system

✅ I can view a user’s borrowing history

✅ I can search for a book by title or author

📽️ Demo Video

[![Watch the video](https://drive.google.com/file/d/1jZKBVU2HN3dyd_lpfLhlDZNmbqqahlbv/view?usp=drive_link)](https://drive.google.com/file/d/1jZKBVU2HN3dyd_lpfLhlDZNmbqqahlbv/view?usp=drive_link)
 
 
