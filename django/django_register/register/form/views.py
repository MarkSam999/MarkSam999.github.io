from from django.contrib.auth.forms import UserC
from django.shortcuts import render

def register(request):
    if request.method == "POST":
        form = U