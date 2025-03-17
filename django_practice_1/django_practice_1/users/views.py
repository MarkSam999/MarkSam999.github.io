from django.shortcuts import render

def first_view(request):
    context = {
        'points': 5832687353
    }
    return render(request, 'users/template.html', context)
