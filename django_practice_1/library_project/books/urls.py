from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.products, name="book_list"),
    path('products/<str>', views.products, name="book_list"),
]