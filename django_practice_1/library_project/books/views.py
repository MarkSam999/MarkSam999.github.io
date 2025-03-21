from django.shortcuts import render
from .models import Book, Product

def products(request, name):
    theName = 
    context = {
        "book_list": Book.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, 'books/products.html', context)
