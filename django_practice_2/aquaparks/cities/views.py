from django.shortcuts import render

def aquaparks(request):
    aquaparks = AquaPark.objects.select_related('city').all()