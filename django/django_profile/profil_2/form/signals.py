from django.dispatch import receiver

@reciever(sender=User)
def create_user_profile(sender, created, **kwargs):
    