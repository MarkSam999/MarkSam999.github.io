from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogView.as_view(), name="logout")
]