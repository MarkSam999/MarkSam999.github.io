from django.shortcuts import render

def aquaparks(request):
    context = {
        'cities': City.objects.all(),
        'aquaparks': AquaPark.objects.all()
    }
    return render(request, "cities/")
