from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q

from .forms import LibroForm
from .models import libros


def lista_libros(request):
    """
    Vista para mostrar el listado de todos los libros.
    Soporta búsqueda por título, autor y filtro por categoría.
    
    RF01 — Consultar libros
    RF02 — Consultar disponibilidad
    RF06 — Buscar libro
    RF07 — Buscar por autor
    RF08 — Filtrar por categoría
    """
    libros_filtrados = libros.copy()
    
    # Obtener búsqueda por título
    buscar_titulo = request.GET.get('titulo', '').strip()
    if buscar_titulo:
        libros_filtrados = [
            libro for libro in libros_filtrados
            if buscar_titulo.lower() in libro['titulo'].lower()
        ]
    
    # Obtener búsqueda por autor
    buscar_autor = request.GET.get('autor', '').strip()
    if buscar_autor:
        libros_filtrados = [
            libro for libro in libros_filtrados
            if buscar_autor.lower() in libro['autor'].lower()
        ]
    
    # Obtener filtro por categoría
    filtro_categoria = request.GET.get('categoria', '').strip()
    if filtro_categoria:
        libros_filtrados = [
            libro for libro in libros_filtrados
            if libro['categoria'].lower() == filtro_categoria.lower()
        ]
    
    # Obtener todas las categorías únicas para el filtro
    categorias = sorted(set(libro['categoria'] for libro in libros))
    
    context = {
        'libros': libros_filtrados,
        'categorias': categorias,
        'buscar_titulo': buscar_titulo,
        'buscar_autor': buscar_autor,
        'filtro_categoria': filtro_categoria,
    }
    
    return render(request, 'library/lista.html', context)


def crear_libro(request):
    """
    Vista para crear un nuevo libro.
    Valida los datos del formulario.
    
    RF03 — Registrar libro
    RF04 — Validar datos
    RF05 — Mostrar nuevo libro
    """
    if request.method == 'POST':
        form = LibroForm(request.POST)
        
        if form.is_valid():
            # Generar nuevo ID
            nuevo_id = max(
                [libro['id'] for libro in libros],
                default=0
            ) + 1
            
            # Crear nuevo libro
            nuevo_libro = {
                'id': nuevo_id,
                'titulo': form.cleaned_data['titulo'],
                'autor': form.cleaned_data['autor'],
                'categoria': form.cleaned_data['categoria'],
                'disponible': form.cleaned_data['disponible'],
            }
            
            # Agregar a la lista
            libros.append(nuevo_libro)
            
            # Redirigir al listado
            return redirect('lista_libros')
    else:
        form = LibroForm()
    
    return render(request, 'library/crear.html', {'form': form})


def detalle_libro(request, libro_id):
    """
    Vista para mostrar los detalles de un libro específico.
    
    RF09 — Mostrar información del libro
    """
    libro = None
    for l in libros:
        if l['id'] == libro_id:
            libro = l
            break
    
    if libro is None:
        raise Http404('El libro no existe')
    
    return render(request, 'library/detalle.html', {'libro': libro})


def editar_libro(request, libro_id):
    """
    Vista para editar un libro existente.
    
    RF11 — Editar información del libro
    """
    libro = None
    indice = None
    for i, l in enumerate(libros):
        if l['id'] == libro_id:
            libro = l
            indice = i
            break
    
    if libro is None:
        raise Http404('El libro no existe')
    
    if request.method == 'POST':
        form = LibroForm(request.POST)
        
        if form.is_valid():
            # Actualizar los datos del libro
            libro['titulo'] = form.cleaned_data['titulo']
            libro['autor'] = form.cleaned_data['autor']
            libro['categoria'] = form.cleaned_data['categoria']
            libro['disponible'] = form.cleaned_data['disponible']
            
            # Redirigir al detalle
            return redirect('detalle_libro', libro_id=libro_id)
    else:
        # Pre-llenar el formulario con los datos actuales
        form = LibroForm(initial={
            'titulo': libro['titulo'],
            'autor': libro['autor'],
            'categoria': libro['categoria'],
            'disponible': libro['disponible'],
        })
    
    return render(request, 'library/editar.html', {
        'form': form,
        'libro': libro
    })


def eliminar_libro(request, libro_id):
    """
    Vista para eliminar un libro.
    Requiere confirmación con POST.
    
    RF12 — Eliminar libro
    """
    libro = None
    indice = None
    for i, l in enumerate(libros):
        if l['id'] == libro_id:
            libro = l
            indice = i
            break
    
    if libro is None:
        raise Http404('El libro no existe')
    
    if request.method == 'POST':
        # Eliminar el libro de la lista
        libros.pop(indice)
        return redirect('lista_libros')
    
    return render(request, 'library/eliminar.html', {'libro': libro})


def actualizar_disponibilidad(request, libro_id):
    """
    Vista para cambiar la disponibilidad de un libro.
    Cambia entre Disponible y Prestado.
    
    RF10 — Actualizar disponibilidad
    """
    libro = None
    for l in libros:
        if l['id'] == libro_id:
            libro = l
            break
    
    if libro is None:
        raise Http404('El libro no existe')
    
    if request.method == 'POST':
        # Cambiar disponibilidad
        libro['disponible'] = not libro['disponible']
        return redirect('detalle_libro', libro_id=libro_id)
    
    return render(request, 'library/actualizar_disponibilidad.html', {'libro': libro})
