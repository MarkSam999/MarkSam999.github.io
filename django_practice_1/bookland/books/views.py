from django.shortcuts import render

def books(request):
    context = {
        'books': 
    }
    return render(request, 'books/index.html', context)
