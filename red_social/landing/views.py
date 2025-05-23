from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from landing.forms import RegisterForm
from django.contrib import messages

#para cookies
from django.http import HttpResponse

#para guardar en la base de datos
from landing.models import Perfil, Publicacion

# Elimina la clase TwoFactorSetupWizard porque ya estamos usando SetupView de two-factor-auth

def index(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'index.html', {'publicaciones': publicaciones})

def register(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te registraste con exito')
            return redirect('login')
    return render(request, 'register.html', {'register_form': register_form})

def Loadlogin(request):
    return redirect('two_factor:login')


def Logout(request):
    logout(request)
    return redirect('index')


def Settings(request):
    return render(request, 'settings.html')

def Posting(request):
    if request.method == 'POST':
        contenido = request.POST['contenido']
        posteo = Publicacion(
            id_user = request.user,
            contenido=contenido,
        )
        print(request.user)
        posteo.save()
        return redirect('index')
    return render(request, 'post.html')

def Account(request):
    return render(request, 'account.html')