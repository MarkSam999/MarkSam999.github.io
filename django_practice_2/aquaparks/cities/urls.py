from django.urls import path
from .views import aquaparks

urlpatterns = [
    path('aquaparks/<int:id>/', aquaparks, name='aquaparks'),
]