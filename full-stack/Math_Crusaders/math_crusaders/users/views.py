from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import EmailAuthenticationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.user.is_authenticated:
        messages.error(request, "You're already registered/logged in.")
        
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Registration passed!")
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "")
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def email_login_view(request):
    if request.user.is_authenticated:
        messages.error(request, "You're already registered/logged in.")
        return redirect('home')
    else:
        if request.method == 'POST':
            form = EmailAuthenticationForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data['user']
                login(request, user)
                return redirect('home')
        else:
            form = EmailAuthenticationForm()

        return render(request, 'users/login.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, 
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Updated!")
            return redirect('profile')
        else:
            print("User form errors:", u_form.errors)
            print("Profile form errors:", p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)