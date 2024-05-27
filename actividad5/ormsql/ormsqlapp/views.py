from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm
from django.db import connection

def clientes_mayores_con_correo_especifico(request):
    correo = request.GET.get('correo', '')
    edad = request.GET.get('edad', '')

    clientes = Cliente.objects.all()

    if edad:
        try:
            edad = int(edad)
            clientes = clientes.filter(edad__gt=edad)
        except ValueError:
            pass

    if correo:
        clientes = clientes.filter(correo=correo)

    return render(request, 'clientes.html', {'clientes': clientes, 'correo': correo, 'edad': edad})

def consulta_sql_raw(request):
    if request.method == 'GET':
        edad = request.GET.get('edad', '')
        if edad:
            try:
                edad = int(edad)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM ormsqlapp_cliente WHERE edad > %s", [edad])
                    clientes = cursor.fetchall()
            except ValueError:
                clientes = []
        else:
            clientes = []

        return render(request, 'clientes.html', {'clientes': clientes})

def invocar_procedimiento_almacenado(request):
    if request.method == 'GET':
        argumento1 = request.GET.get('argumento1', '')
        argumento2 = request.GET.get('argumento2', '')
        if argumento1 and argumento2:
            with connection.cursor() as cursor:
                cursor.callproc('nombre_del_procedimiento', [argumento1, argumento2])
                resultados = cursor.fetchall()
        else:
            resultados = []

        return render(request, 'resultados.html', {'resultados': resultados})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('clientes-mayores')
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})
