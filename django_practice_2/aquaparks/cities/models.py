from django.db import models

class City(models.Model):


    def __str__(self):
        return self.name

class AquaPark(models.Model):


    def __str__(self):
        return self.name