from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)

class Message(models.Model):
    content = models.TextField(
        max_length=100
    )
    publish_time = models.TimeField(
        default=timezone.now
    )
    publish_date = models.DateTimeField(
        default=timezone.now
    )
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content