from django.shortcuts import render
from .models import Book

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)

def details(request, year):
    book = Book.objects.get(year=year)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)
