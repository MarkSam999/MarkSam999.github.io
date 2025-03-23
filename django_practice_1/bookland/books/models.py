from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title