from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, id=None):
    if id:
        city = City.objects.get(id=id)
        aquaparks = AquaPark.objects.filter(city=city)  # Только аквапарки в выбранном городе
    else:
        city = None
        aquaparks = AquaPark.objects.all()  # Все аквапарки

    context = {
        'city': city,
        'cities': City.objects.all(),
        'aquaparks': aquaparks
    }
    return render(request, "cities/index.html", context)