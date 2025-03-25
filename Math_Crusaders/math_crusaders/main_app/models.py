from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class News_Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    content = models.TextField(
        max_length=5000,
    )
    publish_date = models.DateTimeField(
        default=timezone.now
    )
    posted_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_post', kwargs={'pk': self.pk})
    
class Rank(models.Model):
    name = models.CharField(max_length=20)
    emblem = models.ImageField(default='profile_pics/anonymous.png', upload_to='ranks')

    def __str__(self):
        return f'{self.name}'