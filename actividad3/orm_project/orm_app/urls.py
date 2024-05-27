from django.urls import path
from . import views

urlpatterns = [
    # URLs para vistas de productos
    path('productos/', views.ProductoListView.as_view(), name='producto_lista'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('productos/crear/', views.producto_crear, name='producto_crear'),
    path('productos/<int:pk>/editar/', views.producto_editar, name='producto_editar'),

    # URLs para vistas de categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_lista'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detalle'),
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:pk>/editar/', views.categoria_editar, name='categoria_editar'),

    # URLs para vistas de etiquetas
    path('etiquetas/', views.EtiquetaListView.as_view(), name='etiqueta_lista'),
    path('etiquetas/<int:pk>/', views.EtiquetaDetailView.as_view(), name='etiqueta_detalle'),
    path('etiquetas/crear/', views.etiqueta_crear, name='etiqueta_crear'),
    path('etiquetas/<int:pk>/editar/', views.etiqueta_editar, name='etiqueta_editar'),

    # URLs para vistas de perfil
    path('perfil/', views.perfil_detalle, name='perfil_detalle'),
    path('perfil/editar/', views.perfil_editar, name='perfil_editar'),
    path('perfil/crear/', views.perfil_crear, name='perfil_crear'),
]
