class Book:
    """Represents a single book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return  # Stop after checking out
        # No output per test design

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                return  # Stop after returning
        # No output per test design

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
