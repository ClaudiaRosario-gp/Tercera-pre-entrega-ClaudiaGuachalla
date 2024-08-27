from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('inicio/', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('clientes/', views.clientes, name='clientes'),
    path('consultas/', views.consultas, name='consultas'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar/', views.buscar, name='buscar'),
]


