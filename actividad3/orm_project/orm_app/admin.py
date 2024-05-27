from django.contrib import admin
from .models import Categoria, Producto, Etiqueta, Perfil

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Etiqueta)
admin.site.register(Perfil)
