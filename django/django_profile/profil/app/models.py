from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.
    avatar = models.ImageField()
    description = models.TextField(max_length=5000)