from django.shortcuts import render

def view(request):
    context = {
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
