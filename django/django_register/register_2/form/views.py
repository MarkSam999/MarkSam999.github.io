from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def register(request):
    return render(request, "register.html", {"form": form})
