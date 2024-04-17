from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login

def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                if user:
                    login(request, user)
                    return redirect('landing')
                else:
                    return render(request, 'login_logout/signup.html', {
                        'form': CustomUserCreationForm(),
                        'error': 'No se pudo iniciar sesión automáticamente. Intente iniciar sesión manualmente.'
                    })
            except Exception as e:
                return render(request, 'login_logout/signup.html', {
                    'form': CustomUserCreationForm(),
                    'error': f'Ha ocurrido un error: {e}'
                })
        else:
            return render(request, 'login_logout/signup.html', {
                'form': CustomUserCreationForm(request.POST),
                'error': 'La información ingresada no es válida'
            })
    else:
        return render(request, 'login_logout/signup.html', {
            'form': CustomUserCreationForm()
        })

def user_login(request):
    if request.method == 'POST':
        logform = AuthenticationForm(request, request.POST)
        if logform.is_valid():
            username = logform.cleaned_data.get('username')
            password = logform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                error = 'Usuario o contraseña incorrectos'
                return render(request, 'login_logout/login.html', {'logform': logform, 'error': error})
        else:
            error = 'Formulario inválido'
            return render(request, 'login_logout/login.html', {'logform': logform, 'error': error})
    else:
        logform = AuthenticationForm()
        return render(request, 'login_logout/login.html', {'logform': logform})

def cerrar_sesion(request):
    logout(request)
    return redirect("login")

def r(request):
    return render(request, 'login_logout/r.html')