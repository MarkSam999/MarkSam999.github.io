import random

def random_number():
    

def generate_isbn():
    prefix = "978"  # ISBN-13 всегда начинается с 978 или 979
    body = "".join(str(random.randint(0, 9)) for _ in range(9))
    partial_isbn = prefix + body
    check_digit = calculate_isbn13_check_digit(partial_isbn)
    return partial_isbn + check_digit

def calculate_isbn13_check_digit(isbn_without_check_digit):
    total = sum((1 if i % 2 == 0 else 3) * int(num) for i, num in enumerate(isbn_without_check_digit))
    remainder = total % 10
    return str((10 - remainder) % 10)

from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    isbn = models.CharField(unique=True, default=random_number, max_length=13)
