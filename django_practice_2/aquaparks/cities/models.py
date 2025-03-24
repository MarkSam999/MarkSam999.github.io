from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    adress

    def __str__(self):
        return self.name

class AquaPark(models.Model):


    def __str__(self):
        return self.name