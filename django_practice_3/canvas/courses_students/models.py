from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = )
