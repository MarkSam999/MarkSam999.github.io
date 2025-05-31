from . import views
from django.urls import path, include

urlpatterns = [
    path("home", name="home"),
    path("register", name="register"),
    path("login", name="login"),
    path("", name="")
]