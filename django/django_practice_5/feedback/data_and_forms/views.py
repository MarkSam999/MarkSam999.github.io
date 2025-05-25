from django.shortcuts import render, redirect
from .forms import FeedbackForm

def form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeedbackForm()

    return render(request, "index.html", {"form": form})

def success(request):
    return render(request, "success.html")