from . import views
from django.urls import path, include

urlpatterns = [
    path('aquaparks/', aquaparks, name="aquaparks"),
]