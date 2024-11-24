from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class News_Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    content = models.TextField(
        max_length=5000
    )
    publish_date = models.DateTimeField(
        default=timezone.now
    )
    posted_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

class Hist_Event(models.Model):
    title = models.CharField(
        max_length=100
    )
    content = models.TextField(
        max_length=100000
    )

    def __str__(self):
        return self.title