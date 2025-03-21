from django.shortcuts import render
from .models import Book, Product

def products(request, name):
    context = {
        "book_list": Book.objects.all(),
        "thename": theName,
        "products": Product.objects.all()
    }
    return render(request, 'books/products.html', context)