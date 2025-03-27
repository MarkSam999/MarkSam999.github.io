from django.shortcuts import render

def users(request):
    context = {
        'users': User
    }
