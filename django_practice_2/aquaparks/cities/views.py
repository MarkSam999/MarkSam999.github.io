from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, city):
    context = {
        'city': AquaPark.objects.get(city=city),
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html", context)