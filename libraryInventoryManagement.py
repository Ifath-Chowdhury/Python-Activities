# 10.11 Project: Library Inventory Management

# Book class with attributes for title, author, and availability
class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

# Library class with an array of books
class Library:
    def __init__(self):
        self.books = []
    
    def AddBook(self, newBook):
        self.books.append(newBook)
    
    def SearchByAuthor(self, author):
        SearchAuthor = lambda book : book.author.lower() == author.lower()
        return list(filter(SearchAuthor, self.books))

    def SearchByTitle(self, title):
        SearchTitle = lambda book : book.title.lower() == title.lower()
        return list(filter(SearchTitle, self.books))
    
    def UpdateAvailability(self, bookTitle, isAvailable):
        UpdateBookAvailability = lambda book : setattr(book, "availability", isAvailable) if book.title.lower() == bookTitle.lower() else None
        list(map(UpdateBookAvailability, self.books))

# Text functionality with instances of the Book class
book1 = Book("The Bible", "God")
book2 = Book("Dragon Ball", "Akira Toriyama")

library = Library()

library.AddBook(book1)
library.AddBook(book2)

booksByToriyama = library.SearchByAuthor("Akira Toriyama")
print("Books by Akira Toriyama")
for book in booksByToriyama:
    print(book.title)

booksCalledBible = library.SearchByTitle("THe BIble")
print("\nBooks called \"The Bible\":")
for book in booksCalledBible:
    print(book.title)

library.UpdateAvailability("The Bible", False)