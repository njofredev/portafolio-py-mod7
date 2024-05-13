from django.urls import path
from . import views

urlpatterns = [
    path('notas/', views.lista_notas, name='lista_notas'),
]