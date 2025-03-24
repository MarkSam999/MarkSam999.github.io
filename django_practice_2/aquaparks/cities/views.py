from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, id):
    city = City.objects.get(id=id)
    aquaparks = AquaPark.objects.filter(city=city)
    context = {
        'city': city,
        'cities': City.objects.all(),
        'aquaparks': aquaparks
    }
    return render(request, "cities/index.html", context)