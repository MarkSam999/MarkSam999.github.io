from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name="book_list"),
]