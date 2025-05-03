from django.shortcuts import render
from django.db.models import Avg
from .average import products
from .models import Product, Review

def index(request):
    context = {
        'products': Product.objects.annotate(avg_rating=Avg('review__grade'))
    }
    return render(request, "index.html", context)