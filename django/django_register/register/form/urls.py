from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('register', views.register, name="register"),
    path('logout', views.register, name="logout")
]