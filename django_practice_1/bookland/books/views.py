from django.shortcuts import render
from .models import Book

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)

def details(request, title):
    name = Book.objects.get(title=title)
    context = {
        'name': name
    }
    return render(request, 'books/book_detail.html', context)
