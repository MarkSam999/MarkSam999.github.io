from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=1000)
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ManyToManyField(to=Author)
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

