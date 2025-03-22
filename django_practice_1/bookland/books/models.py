from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    year = models.
    description = models.