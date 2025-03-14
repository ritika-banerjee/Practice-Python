class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    

class Library():

    def __init__(self):

        self.books = []

    def add_book(self, book):

        self.books.append(book)
        print(f"{book.title} was added")

    def remove_book(self, isbn):

        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"{book.title} removed successfully")
                return
            
        print("Book not found")

library = Library()

book1 = Book("Red Beans", "Jane Doe", "1")
book2 = Book("Blue cake", "John Doe", "2")

library.add_book(book1)
library.add_book(book2)

library.remove_book("2")
        
        



        