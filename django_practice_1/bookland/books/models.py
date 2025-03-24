from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=1000)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ManyToManyField(Author, related_name="books")
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

