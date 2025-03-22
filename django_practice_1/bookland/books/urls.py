from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name="books"),
    path('books/details/<str:title>', views.details, name="details")
]