from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'blog/login.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

# Profile view
@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        if email:
            user.email = email
            user.save()
            messages.success(request, "Profile updated successfully")
    return render(request, 'blog/profile.html')
