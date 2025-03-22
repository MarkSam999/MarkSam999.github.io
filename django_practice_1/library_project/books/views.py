from django.shortcuts import render
from .models import Book, Product

def books(request):
    context = {
        "book_list": Book.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, 'books/books.html', context)

def products(request, name):
    product = Product.objects.get(name=name)
    context = {
        ''
    }
    return render(request, 'books/products.html', context)