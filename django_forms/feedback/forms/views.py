from django.shortcuts import render
from .forms import ReviewForm

def feedback(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
    return render({'form': form})
