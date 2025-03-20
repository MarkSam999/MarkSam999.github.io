import random

def generate_isbn():
    prefix = "978"  # ISBN-13 всегда начинается с 978 или 979
    body = "".join(str(random.randint(0, 9)) for _ in range(9))
    partial_isbn = prefix + body
    check_digit = calculate_isbn13_check_digit(partial_isbn)
    return partial_isbn + check_digit

from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=13)
