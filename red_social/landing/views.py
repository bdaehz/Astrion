
from urllib import request
from django.shortcuts import render, redirect

#libreria para el auth
from django.contrib.auth import authenticate, login, logout

#formulario de registro
from landing.forms import RegisterForm

#mensaje de que se registro
from django.contrib import messages

# Create your views here.

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
    # if request.method == 'POST':
    #     nombre = request.POST.get('username')
    #     contra = request.POST.get('password')
    #     user = authenticate(request, username = nombre, password = contra)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('index')
    #     else:
    #         messages.warning(request, 'algo no piolo como tenia que piolar')
    #         return redirect('login')
    return redirect('two_factor:login')

def Logout(request):
    logout(request)
    return redirect('index')

