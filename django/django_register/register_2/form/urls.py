from . import views
from django.urls import path, include

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.name="register"),
    path("login", name="login"),
    path("logout", name="logout")
]