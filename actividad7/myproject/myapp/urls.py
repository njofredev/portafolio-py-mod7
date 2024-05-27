from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registration, name='registration'),
    path('inicio/', views.user_login, name='login'),
    path('cerrar-sesion/', views.user_logout, name='logout'),
    path('pagina-especial/', views.special_page, name='special'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'), 
]
