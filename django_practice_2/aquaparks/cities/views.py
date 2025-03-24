from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, id):
    city = City.objects.get(id=id)
    aquaparks = AquaPark.objects.filter(city=city)  # Фильтруем аквапарки по городу

    context = {
        'city': city,
        'cities': City.objects.all(),  # Все города для переключения
        'aquaparks': aquaparks  # Только аквапарки выбранного города
    }
    return render(request, "cities/index.html", context)