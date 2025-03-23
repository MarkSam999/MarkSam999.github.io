from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=1000)
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ManyToManyField(Author, related_name=)
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

