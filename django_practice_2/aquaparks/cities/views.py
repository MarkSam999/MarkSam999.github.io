from django.shortcuts import render, get_object_or_404
from .models import AquaPark, City

def aquaparks(request, id):
    city = get_object_or_404(City, id=id)
    aquaparks = AquaPark.objects.filter(city=city)
    context = {
        'city': city,
        'cities': City.objects.all(),
        'aquaparks': фйгфзфклы
    }
    return render(request, "cities/index.html", context)

def cities(request, id):
    aquapark = AquaPark.objects.get(id=id)    
    context = {
        'city': city,
        'aquapark': aquapark
    }
    return render(request, "cities/cities.html", context)
