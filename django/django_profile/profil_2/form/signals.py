from django.dispatch import receiver
from .models import Profile
from django.

@reciever(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)