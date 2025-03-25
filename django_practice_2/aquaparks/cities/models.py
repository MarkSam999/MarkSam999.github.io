from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f''

class AquaPark(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
