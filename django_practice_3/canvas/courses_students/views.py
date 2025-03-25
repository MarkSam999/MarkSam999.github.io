from django.shortcuts import render
from .models import Course, Student

def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "cour")