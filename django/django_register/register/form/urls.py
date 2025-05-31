from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', LogoutView.as_view(next_page="home"), name="logout")
]