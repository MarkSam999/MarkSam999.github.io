from . import views
from django.urls import path, include
from django.contrib

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", name="login"),
    path("logout", name="logout")
]