from django.db.models import Avg
from list.models import Product, Review
from django.db import models

products = Product.objects.annotate(avg_rating=Avg('review__grade'))

for product in products:
    print(f"{product.name}" + f" - {product.avg_rating}")