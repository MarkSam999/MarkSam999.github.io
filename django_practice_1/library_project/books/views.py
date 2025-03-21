from django.shortcuts import render
from .models import Book, Product

def products(request, name):
    theName = Product.objects.get(name=name)
    context = {
        "book_list": Book.objects.all(),
        "the"
        "products": Product.objects.all()
    }
    return render(request, 'books/products.html', context)
