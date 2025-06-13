from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from landing.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

#para cookies
from django.http import HttpResponse

#para guardar en la base de datos
from landing.models import Perfil, Publicacion

# Elimina la clase TwoFactorSetupWizard porque ya estamos usando SetupView de two-factor-auth

def index(request):
    perfil = Perfil.objects.all()
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'index.html', {'publicaciones': publicaciones, 'photo': perfil})

def register(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            user = register_form.save()
            messages.success(request, 'Te registraste con exito')
            #cuando se crea el usuario se crea la vista del perfil
            perfil = Perfil(
                id_user=user,
                username=user.username,
                photo="https://api.dicebear.com/9.x/dylan/svg?seed="+user.username,
                biografia='Hola estoy usando Astrion que cool😎'
            )
            perfil.save()
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
        imagen = request.FILES.get('imagen')
        posteo = Publicacion(
            id_user = request.user,
            contenido=contenido,
            archivo=imagen
        )
        posteo.save()
        messages.success(request, '¡Publicación creada!')
        return redirect('index')
    return render(request, 'post.html')

def Buscar(request):
    if request.method == 'POST':
        buscar = request.POST["contenido"]
        filtrar = request.POST["filtrar"]
        if(filtrar == "user"):
            perfiles = Perfil.objects.filter(username__icontains=buscar)
            return render(request, 'buscar.html', {'perfiles': perfiles, 'contenido': buscar})
    return render(request, 'buscar.html')

def ver_perfil(request, username):
    user = get_object_or_404(User, username=username)
    perfil = get_object_or_404(Perfil, id_user=user)
    publicaciones = Publicacion.objects.filter(id_user=user).order_by('-fecha')

    return render(request, 'ver_perfil.html', {
        'perfil': perfil,
        'usuario': user,
        'publicaciones': publicaciones
    })

def DeletePost(request, id, volver):
    post = Publicacion.objects.get(pk=id)
    post.delete()
    messages.success(request, 'Se borro con exito el posteo!')
    return redirect(volver)

def EditCuenta(request):
    perfil = get_object_or_404(Perfil, id_user=request.user)

    if request.method == 'POST':
        perfil.biografia = request.POST.get('biografia')
        if request.FILES.get('photo'):
            perfil.photo = request.FILES['photo']
        perfil.save()
        return redirect('ver_perfil', username=request.user.username)  # ajustá esto según tu vista de perfil

    return render(request, 'Edit_account.html', {'perfil': perfil})