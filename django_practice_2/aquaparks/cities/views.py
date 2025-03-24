from django.shortcuts import render
from .models import AquaPark, City

def aquaparks(request):
    aquaparks = AquaPark.objects.select_related('city').all()  # Загружаем все аквапарки вместе с их городами

    context = {
        'aquaparks': aquaparks
    }
    return render(request, "cities/index.html", context)
