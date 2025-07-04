from books.models import Book
from books.models import Author
from datetime import date

a1 = Author(name="Pushkin", biography="a", birth_date = date(1799, 4, 15))
a1.save()

book_1 = Book(title="A Tale of Two Cities", author="Charles Dickens", year=1859, description="Historical fiction")
book_1.save()
book_2 = Book(title="The Little Prince", author="Antoine de Saint-Exupéry", year=1943, description="Fantasy, children's fiction")
book_2.save()
book_3 = Book(title="The Alchemist", author="Paulo Coelho", year=1988, description="Fantasy")
book_3.save()
book_4 = Book(title="Harry Potter and the Philosopher's Stone", author="J. K. Rowling", year=1997, description="Fantasy, children's fiction")
book_4.save()
book_5 = Book(title="And Then There Were None", author="Agatha Christie", year=1939, description="Mystery")
book_5.save()