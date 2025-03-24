from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request):
    context = {
        'city': City.objects.get(int('id=id)),
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/index.html", context)
