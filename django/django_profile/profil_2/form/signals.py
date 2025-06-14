from django.dispatch import receiver
from .models import Profile

@reciever(sender=User)
def create_user_profile(sender, created, **kwargs):
    if created:
        Profile.objects.create(User=instance)