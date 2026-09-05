from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/nuevo/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenadores/<int:id>/editar/', views.editar_entrenador, name='editar_entrenador'),
    path('entrenadores/<int:id>/eliminar/', views.eliminar_entrenador, name='eliminar_entrenador'),
    path('membresias/', views.lista_membresias, name='lista_membresias'),
    path('membresias/nuevo/', views.crear_membresia, name='crear_membresia'),
    path('membresias/<int:id>/editar/', views.editar_membresia, name='editar_membresia'),
    path('membresias/<int:id>/eliminar/', views.eliminar_membresia, name='eliminar_membresia'),
    path('rutinas/', views.lista_rutinas, name='lista_rutinas'),
    path('rutinas/nuevo/', views.crear_rutina, name='crear_rutina'),
    path('rutinas/<int:id>/editar/', views.editar_rutina, name='editar_rutina'),
    path('rutinas/<int:id>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
    path('asistencias/nuevo/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencias/<int:id>/editar/', views.editar_asistencia, name='editar_asistencia'),
    path('asistencias/<int:id>/eliminar/', views.eliminar_asistencia, name='eliminar_asistencia'),
]
