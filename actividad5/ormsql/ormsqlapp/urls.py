from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes_mayores_con_correo_especifico, name='clientes-mayores'),
    path('consulta-sql/', views.consulta_sql_raw, name='consulta-sql'),
    path('invocar-procedimiento/', views.invocar_procedimiento_almacenado, name='invocar-procedimiento'),
    path('crear-cliente/', views.crear_cliente, name='crear-cliente'), 
]
