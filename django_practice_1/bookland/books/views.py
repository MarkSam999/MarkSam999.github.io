from django.shortcuts import render
from .models import Book

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)

def details(request, id):
    title = Book.objects.get(id=id)
    context = {
        'title': title
    }
    return render(request, 'books/book_detail.html', context)
