from django.shortcuts import render
from .models import Book, Author

def books(request):
    context = {
        'books': Book.objects.all()
        'authors': 
    }
    return render(request, 'books/index.html', context)

def details(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)
