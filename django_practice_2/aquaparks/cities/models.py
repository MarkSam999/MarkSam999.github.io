from django.db import models

class AquaPark(models.Model):
    name = models.CharField(max_length=50)
    city = models.Foreign
