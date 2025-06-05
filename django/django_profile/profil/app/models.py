from django.db import models
from django.contrib.auth.

class Profile(models.Model):
    user = models.OneToOneField(User, )