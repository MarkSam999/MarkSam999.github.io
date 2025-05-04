from django.shortcuts import render, redirect
from .forms import ChoiceForm

def choice_form(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ChoiceForm()

    return render(request, "index.html", {"form": form})

def success(request):
    return render(request, "success.html")