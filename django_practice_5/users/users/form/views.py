from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_form(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = RegisterForm()

    return render(request, "index.html", {"form": form})

def success(request):
    return render(request, 'success.html')
