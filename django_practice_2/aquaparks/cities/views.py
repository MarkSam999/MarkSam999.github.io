from django.shortcuts import render
from .models import AquaPark

def aquaparks(request):
    aquaparks = AquaPark.objects.select_related('city').all()
    return render(request, "cities/index.html", {"aquaparks": aquaparks})