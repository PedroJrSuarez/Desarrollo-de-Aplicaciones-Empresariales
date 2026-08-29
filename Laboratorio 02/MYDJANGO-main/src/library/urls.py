from django.urls import path

from . import views


urlpatterns = [
    # Listado de libros
    path('', views.lista_libros, name='lista_libros'),
    
    # Crear libro
    path('crear/', views.crear_libro, name='crear_libro'),
    
    # Detalle de libro
    path('<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    
    # Editar libro
    path('<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    
    # Eliminar libro
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    
    # Cambiar disponibilidad
    path('<int:libro_id>/disponibilidad/', views.actualizar_disponibilidad, name='actualizar_disponibilidad'),
]
