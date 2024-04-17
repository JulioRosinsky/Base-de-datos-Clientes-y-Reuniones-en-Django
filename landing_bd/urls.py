from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('landing/', landing, name='landing'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/eliminar/<int:cliente_id>/', eliminar_cliente, name='clientesdel'),
    path('ejecutivos/', ejecutivos, name='ejecutivos'),
    path('reuniones/<int:reunion_id>/eliminar/', views.eliminar_reunion, name='eliminar_reunion'),
    path('reuniones/', reuniones, name='reuniones'),
    path('agenda/', agenda, name='agenda'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('familia/crear', crear_familia, name='crear_familia'),
    path('familias/crear/crear_sociedades/', crear_sociedades, name='crear_sociedades'),
    path('clientes/crear/crear_sociedades/<int:sociedad_id>/eliminar/', eliminar_sociedades, name='eliminar_sociedades'),
    path('clientes/crear/crear_sociedades/<int:sociedad_id>/', hoja_sociedad, name='hoja_sociedades'),
    path('familia/buscar', buscar_familias, name='buscar_familia'),
    path('familia/<int:familia_id>/', detalles_familia, name='detalles_familia'),
    path('familia/', familia, name='familia'),
    path('familia/<int:familia_id>/eliminar', eliminar_familia, name='familiadel'),
    path('clientes/crear/buscar', buscar_clientes, name='buscar_clientes'),
    path('reuniones/crear/', crear_reuniones, name='crear_reuniones'),
    path('reuniones/crear/buscar', buscar_reuniones, name='buscar_reuniones'),
    path('clientes/<int:cliente_id>/', views.detalles_cliente, name='detalles_cliente'),
    path('reuniones/<int:reunion_id>/', views.detalles_reuniones, name='detalles_reunion'),
    path('clientes/exportar/', views.exportar_clientes, name='exportar_cliente'),
    path('clientes/importar/', views.importar_cliente, name='importar_clientes'),
    path('reuniones/exportar/', views.exportar_reuniones, name='exportar_reuniones'),
]
