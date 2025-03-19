from django.shortcuts import render
from . import models

def book_list(request):
    context = {
        "book_list": Book.objects.all()
    }
