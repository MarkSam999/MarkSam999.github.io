from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import User
from .models import Profile

@receiver