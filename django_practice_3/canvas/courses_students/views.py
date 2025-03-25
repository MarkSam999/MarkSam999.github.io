from django.shortcuts import render
from .models import Course, Student

def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses_students/courses.html", context)

def students(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, "courses_students/students.html", context)