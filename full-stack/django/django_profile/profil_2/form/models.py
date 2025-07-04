from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    bio = models.TextField(max_length=5000)
    rating = models.IntegerField(default=1000)
