from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Categoria, Producto, Etiqueta, Perfil
from .forms import ProductoForm, PerfilForm, CategoriaForm, EtiquetaForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'orm_app/producto_lista.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'orm_app/producto_detalle.html'
    context_object_name = 'producto'

def perfil_detalle(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    return render(request, 'orm_app/perfil_detalle.html', {'perfil': perfil})

def perfil_editar(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil_detalle')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'orm_app/perfil_editar.html', {'form': form})

def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'orm_app/producto_crear.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'orm_app/producto_editar.html', {'form': form})

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'orm_app/categoria_lista.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'orm_app/categoria_detalle.html'
    context_object_name = 'categoria'

def categoria_crear(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()
    return render(request, 'orm_app/categoria_crear.html', {'form': form})

def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'orm_app/categoria_editar.html', {'form': form})

class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'orm_app/etiqueta_lista.html'
    context_object_name = 'etiquetas'

class EtiquetaDetailView(DetailView):
    model = Etiqueta
    template_name = 'orm_app/etiqueta_detalle.html'
    context_object_name = 'etiqueta'

def etiqueta_crear(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_lista')
    else:
        form = EtiquetaForm()
    return render(request, 'orm_app/etiqueta_crear.html', {'form': form})

def etiqueta_editar(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_lista')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'orm_app/etiqueta_editar.html', {'form': form})


def perfil_crear(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil_detalle')
    else:
        form = PerfilForm()
    return render(request, 'orm_app/perfil_crear.html', {'form': form})