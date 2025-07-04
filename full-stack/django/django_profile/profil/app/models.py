from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15)
    avatar = models.ImageField()
    description = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)

    def __init__(self):
        return self.nickname