from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request):
    context = {
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html")
