from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import UserProfile

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            user = UserProfile.objects.create_user(username=username, password=password, email=email)
            messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
            return redirect('login')
    return render(request, 'registration.html')

def custom_user_check(user):
    # Ejemplo de función para user_passes_test
    return user.is_staff

@login_required
@user_passes_test(custom_user_check)
def special_page(request):
    return render(request, 'special.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, '¡Has cerrado sesión exitosamente!')
    return redirect('login')

def home(request):
    return render(request, 'home.html')
