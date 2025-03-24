from . import views
from django.urls import path, include

urlpatterns = [
    path('/aquaparks', views.aquaparks, name="aquaparks"),
    path('/cities', views.cities, name="cities"),
]