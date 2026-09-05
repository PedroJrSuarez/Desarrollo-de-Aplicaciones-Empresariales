from django.shortcuts import get_object_or_404, redirect, render

from .forms import AsistenciaForm, ClienteForm, EntrenadorForm, MembresiaForm, RutinaForm
from .models import Asistencia, Cliente, Entrenador, Membresia, Rutina


def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_entrenadores': Entrenador.objects.count(),
        'total_membresias': Membresia.objects.count(),
        'total_rutinas': Rutina.objects.count(),
        'total_asistencias': Asistencia.objects.count(),
    }
    return render(request, 'gimnasio/inicio.html', context)


def _lista(request, modelo, template, nombre, orden='id'):
    return render(request, template, {nombre: modelo.objects.all().order_by(orden)})


def _formulario(request, modelo, formulario, lista_url, objeto_id=None):
    objeto = get_object_or_404(modelo, id=objeto_id) if objeto_id else None
    form = formulario(request.POST or None, instance=objeto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(lista_url)
    return render(request, 'gimnasio/formulario.html', {'form': form, 'titulo': 'Editar' if objeto else 'Nuevo'})


def _eliminar(request, modelo, objeto_id, lista_url):
    objeto = get_object_or_404(modelo, id=objeto_id)
    if request.method == 'POST':
        objeto.delete()
        return redirect(lista_url)
    return render(request, 'gimnasio/confirmar_eliminar.html', {
        'objeto': objeto, 'cancelar_url': lista_url,
    })


def lista_clientes(request):
    return _lista(request, Cliente, 'gimnasio/clientes/lista.html', 'clientes', 'apellido')


def crear_cliente(request):
    return _formulario(request, Cliente, ClienteForm, 'lista_clientes')


def editar_cliente(request, id):
    return _formulario(request, Cliente, ClienteForm, 'lista_clientes', id)


def eliminar_cliente(request, id):
    return _eliminar(request, Cliente, id, 'lista_clientes')


def lista_entrenadores(request):
    return _lista(request, Entrenador, 'gimnasio/entrenadores/lista.html', 'entrenadores', 'apellido')


def crear_entrenador(request):
    return _formulario(request, Entrenador, EntrenadorForm, 'lista_entrenadores')


def editar_entrenador(request, id):
    return _formulario(request, Entrenador, EntrenadorForm, 'lista_entrenadores', id)


def eliminar_entrenador(request, id):
    return _eliminar(request, Entrenador, id, 'lista_entrenadores')


def lista_membresias(request):
    membresias = Membresia.objects.all().order_by('-fecha_inicio')
    return render(request, 'gimnasio/membresias/lista.html', {'membresias': membresias})


def crear_membresia(request):
    return _formulario(request, Membresia, MembresiaForm, 'lista_membresias')


def editar_membresia(request, id):
    return _formulario(request, Membresia, MembresiaForm, 'lista_membresias', id)


def eliminar_membresia(request, id):
    return _eliminar(request, Membresia, id, 'lista_membresias')


def lista_rutinas(request):
    rutinas = Rutina.objects.select_related('cliente', 'entrenador').order_by('nombre')
    return render(request, 'gimnasio/rutinas/lista.html', {'rutinas': rutinas})


def crear_rutina(request):
    return _formulario(request, Rutina, RutinaForm, 'lista_rutinas')


def editar_rutina(request, id):
    return _formulario(request, Rutina, RutinaForm, 'lista_rutinas', id)


def eliminar_rutina(request, id):
    return _eliminar(request, Rutina, id, 'lista_rutinas')


def lista_asistencias(request):
    asistencias = Asistencia.objects.select_related('cliente').order_by('-fecha', '-hora_entrada')
    return render(request, 'gimnasio/asistencias/lista.html', {'asistencias': asistencias})


def crear_asistencia(request):
    return _formulario(request, Asistencia, AsistenciaForm, 'lista_asistencias')


def editar_asistencia(request, id):
    return _formulario(request, Asistencia, AsistenciaForm, 'lista_asistencias', id)


def eliminar_asistencia(request, id):
    return _eliminar(request, Asistencia, id, 'lista_asistencias')
