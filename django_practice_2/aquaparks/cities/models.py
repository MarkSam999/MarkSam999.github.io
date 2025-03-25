from django.db import models

class City(models.Model):
    name = models.CharField()

class AquaPark(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
