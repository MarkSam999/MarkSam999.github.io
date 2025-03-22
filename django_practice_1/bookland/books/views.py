from django.shortcuts import render

def books(request):
    context = {
        
    }
    return render(request, 'books/index.html', context)
