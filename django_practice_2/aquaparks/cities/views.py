from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request, id):
    context = {
        'cities': City.objects.get(id=id),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html", context)