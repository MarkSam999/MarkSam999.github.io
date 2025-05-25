from . import views
from django.urls import path

urlpatterns = [
    path('form/', views.register_form, name="register_form"),
    path('success/', views.success, name="success")
]