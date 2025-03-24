from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, id):
    city = City.objects.get(id=id)
    aq
    context = {
        'city': city,
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html", context)