from django.shortcuts import render
from .models import Nota

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notasApp/lista_notas.html', {'notas': notas})