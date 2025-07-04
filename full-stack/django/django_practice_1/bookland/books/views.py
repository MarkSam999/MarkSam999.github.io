from django.shortcuts import render
from .models import Book, Author

def books(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all()
    }
    return render(request, 'books/index.html', context)

def details(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=id)
    context = {
        'book': book,
        'author': author
    }
    return render(request, 'books/book_detail.html', context)
