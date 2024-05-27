from django.urls import path
from .views import lista_productos, crear_producto, editar_producto, confirmar_eliminacion

urlpatterns = [
    path('productos/', lista_productos, name='lista-productos'),
    path('productos/nuevo/', crear_producto, name='crear-producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar-producto'),
    path('productos/eliminar/<int:pk>/', confirmar_eliminacion, name='confirmar-eliminacion'),
]
