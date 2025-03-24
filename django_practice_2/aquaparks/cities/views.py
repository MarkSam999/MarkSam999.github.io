from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request):
    context = {
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html")

def cities(request):
    city = City.objects.get(id=id)
    aquapark = AquaPark.objects.get(id=id)    
    context = {
        'city': city,
        'aquapark': aquapark
    }
    return render(request, "cities/index.html")
