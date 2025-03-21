import random

def random_number():
    int = "".join(str(random.randint(0, 9)) for _ in range(13))
    return int

from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    isbn = models.CharField(unique=True, default=random_number, max_length=13)

class Product(models.Model):
    name = CharFirld