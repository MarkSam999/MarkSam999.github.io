from django.shortcuts import render

def first_view(request):
    context = {
        'points': 5
    }
    return render(request, 'users/template.html', context)
