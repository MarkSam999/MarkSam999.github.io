from . import views
from django.urls import path

urlpatterns = [
    path("form", views.form, name="form"),
    path("success", views.success, name="success")
]