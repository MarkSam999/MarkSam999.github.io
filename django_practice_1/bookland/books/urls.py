from django.urls import path
from . import views

urlpatterns = [
    path(', views.books, name="books"),
    path('/<str:title>', views.details, name="details")
]