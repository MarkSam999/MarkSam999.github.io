from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    grade = models.IntegerField()
    text = models.TextField(max_length=1000)