from django import forms
from .models import Producto, Perfil, Categoria, Etiqueta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
