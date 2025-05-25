from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('home', views.home),
    path('register', views.register, name="r