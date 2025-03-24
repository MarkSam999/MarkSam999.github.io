from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

class AquaPark(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    description = models.TextField(max_length=5000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name