from books.models import Book
from books.models import random_number
from datetime import date

book_1 = Book(title='Frankenstein', author='Mary Shelley')
book_1.save()
book_2 = Book(title='Prometheus Unbound', author='Percy Bysshe Shelley')
book.save()
book_3 = Book(title='Minekampf', author='Adolf Hitler')
book.save()
book_4 = Book(title='Refusal of Slavery', author='US Government', published_date=date(1865,6,18))
book.save()
book_5 = Book(title='Molotov-Ribbentrop Pact', author='Joseph Stalin and Adolf Hitler')
book.save()