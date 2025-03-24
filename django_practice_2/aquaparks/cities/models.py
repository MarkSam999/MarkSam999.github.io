from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)
    
    addressdescription = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

class AquaPark(models.Model):


    def __str__(self):
        return self.name