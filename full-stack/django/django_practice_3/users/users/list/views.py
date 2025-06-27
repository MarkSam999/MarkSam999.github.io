from django.shortcuts import render
from .models import User

def users(request):
    context = {
        'users': User.objects.all().order_by('username')
    }
    return render(request, "list/index.html", context)
