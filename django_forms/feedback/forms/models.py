from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    movie_title = models.CharField()
