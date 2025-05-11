from django.db import models
from django import Q

class Review(models.Model):
    name = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)