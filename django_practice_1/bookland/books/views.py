from django.shortcuts import render

def books(request):
    return render(request, 'books/index.html', context)
