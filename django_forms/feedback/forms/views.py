from django.shortcuts import render
from .forms import ReviewForm

def feedback(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = ReviewForm()
    return render(request, "index.html", {'form': form})

def reviews(request):
    context = {
        'review_list': 
    }
