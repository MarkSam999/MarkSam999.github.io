from django.shortcuts import render
from .models import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
    return render({'form': form})
