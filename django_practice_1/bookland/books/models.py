from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=1000, blank=True)
    birth_date = models.DateField(blank=True)

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ManyToManyField(Author)
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

