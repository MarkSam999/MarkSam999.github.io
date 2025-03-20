from books.models import Book
from books.models import random_number
from datetime import date

book_ = Book(title='Frankenstein', author='Mary Shelley')
book_ = Book(title='Prometheus Unbound', author='Percy Bysshe Shelley')
book_ = Book(title='Minekampf', author='Adolf Hitler')
book_ = Book(title='Refusal of Slavery', author='US Government', published_date=date(1865,6,18))
book_ = Book(title='Molotov-Ribbentrop Pact', author='Joseph Stalin and Adolf Hitler')