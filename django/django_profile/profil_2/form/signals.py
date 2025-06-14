from django.dispatch import receiver

@reciever()
def create_user_profile(created, **kwargs)