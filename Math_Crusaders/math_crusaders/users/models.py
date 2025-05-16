from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Rank(models.Model):
    name = models.CharField(max_length=20)
    emblem = models.ImageField(default='profile_pics/anonymous.png', upload_to='ranks')

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/anonymous.png', upload_to='profile_pics')
    coins = models.IntegerField(default=0)
    rating = models.IntegerField(default=100)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, default=1, related_name="profiles")
    style = models.ForeignKey(Style, on_delete=models.CASCADE, default=1, related_name="profiles", choices=)

    def __str__(self):
        return f'{self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

