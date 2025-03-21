from django.shortcuts import render
from .models import Book, Product

def book_list(request):
    context = {
        "book_list": Book.objects.all()
        "product": Product.objects.all()
    }
    return render(request, 'books/book_list.html', context)
