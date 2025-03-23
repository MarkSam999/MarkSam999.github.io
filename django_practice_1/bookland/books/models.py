from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ManyToManyField()
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

class Author(models.Model):
    name = models.CharField(max_length=50)