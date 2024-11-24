from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"{username}, you've passed the registration!")
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})