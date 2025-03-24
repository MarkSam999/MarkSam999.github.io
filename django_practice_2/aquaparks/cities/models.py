from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=)

    def __str__(self):
        return self.name

class AquaPark(models.Model):


    def __str__(self):
        return self.name