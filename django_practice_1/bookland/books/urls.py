from django.urls import path
from . import booksviews

urlpatterns = [
    path('books/', books)
]