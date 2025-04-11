from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from landing.forms import RegisterForm
from django.contrib import messages

# Elimina la clase TwoFactorSetupWizard porque ya estamos usando SetupView de two-factor-auth

def index(request):
    return render(request, 'index.html')

def register(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te registraste papu :vv')
            return redirect('index')
    return render(request, 'register.html', {'register_form': register_form})

def Loadlogin(request):
    return redirect('two_factor:login')

def Logout(request):
    logout(request)
    return redirect('index')
