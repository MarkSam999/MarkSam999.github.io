from django.shortcuts import render
from .models import Book, Product

def book_list(request):
    context = {
        "book_list": Book.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, 'books/products.html', context)
