from from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    if request.method == "POST":
        form = Use