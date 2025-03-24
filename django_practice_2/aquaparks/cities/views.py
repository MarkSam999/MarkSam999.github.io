from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request):
    context = {
        'city': AquaPark.objects.get(city.name==city.name),
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html", context)