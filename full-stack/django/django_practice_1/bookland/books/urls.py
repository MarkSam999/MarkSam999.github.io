from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('<int:id>', views.details, name="details")
]