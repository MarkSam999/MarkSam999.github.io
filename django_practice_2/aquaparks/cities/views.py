from django.shortcuts import render, get_object_or_404
from .models import AquaPark, City

def aquaparks(request, id):
    city = get_object_or_404(City, id=id)
    aquaparks = AquaPark.objects.filter(city=city)
    context = {
        'city': city,
        'cities': City.objects.all(),
        'aquaparks': aquaparks
    }
    return render(request, "cities/index.html", context)
