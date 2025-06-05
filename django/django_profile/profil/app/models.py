from django.db import models
from django.

class Profile(models.Model):
    user = models.OneToOneField(User, )