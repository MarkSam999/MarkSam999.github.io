from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('<h1>Welcome</h1>')

def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1>')

def history(request):
    return HttpResponse('<h1>The history of "Math Crusaders"</h1>')

def news(request):
    return HttpResponse('<h1>Fresh News</h1>')