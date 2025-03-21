from books.models import Book, Product
from books.models import random_number
from datetime import date

book_1 = Book(title='Frankenstein', author='Mary Shelley')
book_1.save()
book_2 = Book(title='Prometheus Unbound', author='Percy Bysshe Shelley')
book_2.save()
book_3 = Book(title='Minekampf', author='Adolf Hitler')
book_3.save()
book_4 = Book(title='Refusal of Slavery', author='US Government', published_date=date(1865,6,18))
book_4.save()
book_5 = Book(title='Molotov-Ribbentrop Pact', author='Joseph Stalin and Adolf Hitler')
book_5.save()

product_1 = Product(name="milk", price=2.50, description="", available=True)
product_1.save()
product_2 = Product(name="cheese", price=, description="", available=True)
product_2.save()
product_3 = Product(name="bread", price=, description="", available=True)
product_3.save()
product_4 = Product(name="candy", price=, description="", available=True)
product_4.save()