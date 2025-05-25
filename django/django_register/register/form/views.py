from from django.contrib.auth
from django.shortcuts import render

def register(request):
    if request.method == "POST":
        form = U