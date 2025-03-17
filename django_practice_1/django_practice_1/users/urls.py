from django.urls import path
from . import views

urlpatterns = [
    path('first_view/', views.first_view, name='first_view')
]