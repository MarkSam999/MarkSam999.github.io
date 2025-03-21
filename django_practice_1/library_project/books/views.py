from django.shortcuts import render
from .models import Book

def book_list(request):
    context = {
        "book_list": Book.objects.all()
        "product": Pro
    }
    return render(request, 'books/book_list.html', context)
