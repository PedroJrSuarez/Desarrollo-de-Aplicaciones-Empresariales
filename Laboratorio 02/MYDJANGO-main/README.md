# Laboratorio 02 — Aplicación Django: Biblioteca

## Información general

**Curso:** Desarrollo de Aplicaciones Empresariales <br>
**Integrantes:** Gonzalo Davila y Pedro Suarez  
**Laboratorio:** 02 — Clases, atributos y métodos  
**Tecnología:** Python 3.10+, Django 5, Visual Studio Code y GitHub  
**Problemática:** Consulta y registro de libros de una biblioteca.

> **Importante:** El laboratorio trabaja con datos estáticos en memoria. No se utilizará una base de datos, migraciones ni el panel de administración de Django. Los datos agregados mediante el formulario se perderán cuando se reinicie el servidor.

# PROGRAMA EN FUNCIONAMIENTO

<img width="1185" height="892" alt="image" src="https://github.com/user-attachments/assets/be6893c4-0092-4d24-a97d-3f6672e59f17" />

---

# EJERCICIO 1 — Investigar una problemática real

## Problemática

En una biblioteca, los usuarios pueden perder tiempo buscando un libro en los estantes sin saber si se encuentra disponible. Esto puede generar molestias cuando finalmente descubren que el libro ya fue prestado. La aplicación permitirá consultar los libros y conocer su disponibilidad antes de buscarlos físicamente. El sistema será utilizado por los usuarios y el personal encargado de la biblioteca.

## Objetivo

Desarrollar una aplicación web utilizando Django que permita consultar los libros registrados en una biblioteca, conocer su disponibilidad y registrar nuevos libros mediante un formulario.

---

# EJERCICIO 2 — Capturar los requisitos

A partir de la problemática identificada, se establecen los siguientes requisitos funcionales:

### RF01 — Consultar libros

El sistema debe permitir a los usuarios visualizar el listado de libros registrados en la biblioteca.

### RF02 — Consultar disponibilidad

El sistema debe permitir a los usuarios conocer si un libro se encuentra disponible o prestado.

### RF03 — Registrar libro

El sistema debe permitir al personal encargado registrar un nuevo libro indicando sus datos principales.

### RF04 — Validar datos

El sistema debe validar que los campos obligatorios del formulario de registro sean completados correctamente.

### RF05 — Mostrar nuevo libro

El sistema debe mostrar en el listado el nuevo libro después de que haya sido registrado correctamente.

### RF06 — Buscar libro

El sistema debe permitir a los usuarios buscar un libro por su título para encontrarlo rápidamente dentro del listado.

### RF07 — Buscar por autor

El sistema debe permitir a los usuarios buscar libros mediante el nombre del autor.

### RF08 — Filtrar por categoría

El sistema debe permitir filtrar los libros según su categoría.

### RF09 — Mostrar información del libro

El sistema debe permitir visualizar la información principal de un libro seleccionado, como título, autor, categoría y disponibilidad.

### RF10 — Actualizar disponibilidad

El sistema debe permitir al personal encargado actualizar el estado de disponibilidad de un libro entre disponible y prestado.

### RF11 — Editar información del libro

El sistema debe permitir al personal encargado modificar la información registrada de un libro.

### RF12 — Eliminar libro

El sistema debe permitir al personal encargado eliminar un libro del listado cuando ya no forme parte de la biblioteca.

---

# EJERCICIO 3 — Diseñar el modelo de datos

## Entidad principal: Libro

La entidad principal del sistema será `Libro`.

| Campo | Tipo de dato | Obligatorio | Justificación |
|---|---|---|---|
| `id` | Entero | Sí | Permite identificar de manera única cada libro registrado. |
| `titulo` | Texto | Sí | Permite conocer el nombre del libro que el usuario desea buscar. |
| `autor` | Texto | Sí | Permite identificar al autor del libro y facilitar su consulta. |
| `categoria` | Texto | Sí | Permite clasificar los libros según su temática o tipo. |
| `disponible` | Booleano | Sí | Permite indicar si el libro está disponible o actualmente prestado. |

## Representación de los datos

Debido a que el laboratorio no utiliza una base de datos, los libros serán almacenados mediante una lista de diccionarios dentro de `models.py`.

Ejemplo:

```python
libros = [
    {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "categoria": "Novela",
        "disponible": True
    }
]
```

---

# EJERCICIO 4 — Crear la nueva App

Dentro del proyecto Django existente se creará una nueva aplicación llamada:

```text
library
```

La aplicación estará relacionada con la problemática de la biblioteca.

## Crear la aplicación

Desde la carpeta donde se encuentra `manage.py`:

```powershell
python manage.py startapp library
```

## Registrar la App

Abrir:

```text
src/config/settings.py
```

Agregar `library` dentro de `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "core",
    "library",
]
```

## Estructura esperada

```text
Proyecto/
│
├── .venv/
│
├── src/
│   ├── manage.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── core/
│   │   └── ...
│   │
│   └── library/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── views.py
│       ├── urls.py
│       ├── forms.py
│       │
│       └── templates/
│           └── library/
│               ├── lista.html
│               └── crear.html
│
├── requirements.txt
└── README.md
```

---

# EJERCICIO 5 — Implementar el Model con datos estáticos

En este laboratorio no se utilizará un modelo tradicional de Django con `models.Model`.

Los datos estarán almacenados en una lista de diccionarios.

Archivo:

```text
src/library/models.py
```

Código:

```python
libros = [
    {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "categoria": "Novela",
        "disponible": True,
    },
    {
        "id": 2,
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "categoria": "Clásico",
        "disponible": False,
    },
    {
        "id": 3,
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "categoria": "Literatura",
        "disponible": True,
    },
    {
        "id": 4,
        "titulo": "1984",
        "autor": "George Orwell",
        "categoria": "Ciencia ficción",
        "disponible": True,
    },
    {
        "id": 5,
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "categoria": "Romance",
        "disponible": False,
    },
]
```

## Consideraciones

Los datos se almacenan solamente en memoria.

Por este motivo:

- No se utilizarán migraciones.
- No se utilizará una base de datos.
- No se utilizará `ModelForm`.
- Los datos registrados mediante el formulario se perderán al reiniciar el servidor.
- La lista `libros` será la fuente de datos de la aplicación.

---

# EJERCICIO 6 — Implementar el listado

## 6.1 Crear la View

Archivo:

```text
src/library/views.py
```

Código:

```python
from django.shortcuts import render

from .models import libros


def lista_libros(request):
    return render(
        request,
        "library/lista.html",
        {"libros": libros}
    )
```

Esta vista obtiene los libros desde `models.py` y los envía al template.

---

## 6.2 Crear las URLs de la App

Archivo:

```text
src/library/urls.py
```

Código:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista_libros, name="lista_libros"),
]
```

---

## 6.3 Conectar la App con el proyecto

Abrir:

```text
src/config/urls.py
```

Agregar la ruta de `library`:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("library/", include("library.urls")),
]
```

La aplicación podrá abrirse en:

```text
http://127.0.0.1:8000/library/
```

---

## 6.4 Crear el Template

Crear:

```text
src/library/templates/library/lista.html
```

Código:

```html
{% extends "base.html" %}

{% block content %}

<h1>Biblioteca</h1>

<a href="{% url 'crear_libro' %}">
    Registrar nuevo libro
</a>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Autor</th>
            <th>Categoría</th>
            <th>Disponibilidad</th>
        </tr>
    </thead>

    <tbody>
        {% for libro in libros %}
        <tr>
            <td>{{ libro.id }}</td>
            <td>{{ libro.titulo }}</td>
            <td>{{ libro.autor }}</td>
            <td>{{ libro.categoria }}</td>

            <td>
                {% if libro.disponible %}
                    Disponible
                {% else %}
                    Prestado
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}
```

---

# EJERCICIO 7 — Implementar el formulario

Se creará un formulario utilizando `forms.Form`.

No se utilizará `ModelForm`, debido a que no existe una base de datos.

Crear:

```text
src/library/forms.py
```

Código:

```python
from django import forms


class LibroForm(forms.Form):

    titulo = forms.CharField(
        label="Título",
        max_length=200,
        required=True
    )

    autor = forms.CharField(
        label="Autor",
        max_length=150,
        required=True
    )

    categoria = forms.CharField(
        label="Categoría",
        max_length=100,
        required=True
    )

    disponible = forms.BooleanField(
        label="Disponible",
        required=False
    )
```

## Campos del formulario

El formulario permitirá ingresar:

- Título.
- Autor.
- Categoría.
- Disponibilidad.

Los campos `titulo`, `autor` y `categoria` son obligatorios.

---

# EJERCICIO 8 — Implementar la vista de creación

Modificar:

```text
src/library/views.py
```

Código completo:

```python
from django.shortcuts import redirect, render

from .forms import LibroForm
from .models import libros


def lista_libros(request):
    return render(
        request,
        "library/lista.html",
        {"libros": libros}
    )


def crear_libro(request):

    if request.method == "POST":

        form = LibroForm(request.POST)

        if form.is_valid():

            nuevo_id = max(
                [libro["id"] for libro in libros],
                default=0
            ) + 1

            nuevo_libro = {
                "id": nuevo_id,
                "titulo": form.cleaned_data["titulo"],
                "autor": form.cleaned_data["autor"],
                "categoria": form.cleaned_data["categoria"],
                "disponible": form.cleaned_data["disponible"],
            }

            libros.append(nuevo_libro)

            return redirect("lista_libros")

    else:
        form = LibroForm()

    return render(
        request,
        "library/crear.html",
        {"form": form}
    )
```

---

## Actualizar las URLs

Abrir:

```text
src/library/urls.py
```

Utilizar:

```python
from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista_libros, name="lista_libros"),
    path("crear/", views.crear_libro, name="crear_libro"),
]
```

---

## Crear el Template del formulario

Crear:

```text
src/library/templates/library/crear.html
```

Código:

```html
{% extends "base.html" %}

{% block content %}

<h1>Registrar libro</h1>

<form method="post">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Registrar libro
    </button>

</form>

<a href="{% url 'lista_libros' %}">
    Volver al listado
</a>

{% endblock %}
```

---

## Funcionamiento

El proceso será:

```text
Usuario
   ↓
Formulario
   ↓
POST
   ↓
View crear_libro
   ↓
Validación
   ↓
Agregar libro a la lista
   ↓
Redirect
   ↓
Listado
```

Después de registrar correctamente el libro, el usuario será redirigido al listado.

El nuevo registro aparecerá en la lista mientras el servidor continúe ejecutándose.

---

# EJERCICIO 9 — Verificación del flujo completo

## Flujo MVT

La aplicación utilizará el patrón MVT de Django.

```text
REQUEST
   │
   ▼
URL
   │
   ▼
VIEW
   │
   ▼
MODEL
(datos estáticos)
   │
   ▼
TEMPLATE
   │
   ▼
RESPONSE
```

---

## Caso 1 — Consultar libros

El usuario ingresa:

```text
http://127.0.0.1:8000/library/
```

Django recibe la solicitud.

La URL:

```text
/library/
```

ejecuta:

```python
views.lista_libros
```

La vista obtiene los datos desde:

```text
library/models.py
```

Después, los datos son enviados al template:

```text
library/lista.html
```

Finalmente, Django genera una respuesta HTML que se muestra en el navegador.

---

## Caso 2 — Registrar un libro

El usuario selecciona:

```text
Registrar nuevo libro
```

Django abre:

```text
/library/crear/
```

El usuario completa el formulario.

Al presionar:

```text
Registrar libro
```

se envía una solicitud:

```text
POST
```

La vista:

```python
crear_libro()
```

recibe los datos.

Después se ejecuta:

```python
form.is_valid()
```

Si los datos son correctos, se crea un nuevo diccionario:

```python
nuevo_libro = {
    "id": nuevo_id,
    "titulo": form.cleaned_data["titulo"],
    "autor": form.cleaned_data["autor"],
    "categoria": form.cleaned_data["categoria"],
    "disponible": form.cleaned_data["disponible"],
}
```

Luego se agrega a la lista:

```python
libros.append(nuevo_libro)
```

Finalmente se ejecuta:

```python
return redirect("lista_libros")
```

El usuario vuelve al listado y puede observar el nuevo libro.

---

## Convivencia entre `core` y `library`

La aplicación `library` forma parte del mismo proyecto Django que la aplicación `core`.

La estructura general es:

```text
Proyecto Django
│
├── config
│   └── Configuración general
│
├── core
│   └── Funcionalidades existentes
│
└── library
    └── Funcionalidades de biblioteca
```

Cada aplicación mantiene sus propios archivos:

```text
models.py
views.py
urls.py
forms.py
templates/
```

El archivo:

```text
config/urls.py
```

permite conectar las diferentes aplicaciones dentro del proyecto.

Por ejemplo:

```python
path("library/", include("library.urls")),
```

permite acceder a las funcionalidades de `library`.

---

## Capturas de evidencia

Para demostrar el funcionamiento de la aplicación se deben realizar capturas de pantalla.

### Captura 1 — Listado de libros

Debe mostrar:

- La URL `/library/`.
- Los libros registrados.
- El título.
- El autor.
- La categoría.
- La disponibilidad.

### Captura 2 — Formulario

Debe mostrar:

- La URL `/library/crear/`.
- Los campos del formulario.
- El botón para registrar.

### Captura 3 — Nuevo registro

Registrar un nuevo libro y mostrar nuevamente el listado.

La captura debe demostrar que el nuevo libro fue agregado correctamente.

### Captura 4 — Código

Mostrar los principales archivos:

```text
models.py
forms.py
views.py
urls.py
lista.html
crear.html
```

---

# EJERCICIO 10 — Publicar en GitHub

## Actualizar requirements.txt

Verificar que Django esté incluido.

Ejemplo:

```text
Django>=5,<6
```

También puede generarse automáticamente mediante:

```powershell
pip freeze > requirements.txt
```

---

## Actualizar README.md

El `README.md` debe describir:

- La problemática seleccionada.
- Los requisitos funcionales.
- La entidad principal.
- Los campos de la entidad.
- La App `library`.
- El funcionamiento del formulario.
- El flujo MVT.
- La integración con `core`.
- La utilización de datos estáticos.
- La limitación de que los datos se pierden al reiniciar el servidor.

---

# Verificación antes de realizar el commit

Desde la carpeta donde se encuentra `manage.py`, ejecutar:

```powershell
python manage.py check
```

Si no aparecen errores:

```powershell
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/library/
```

## Lista de comprobación

- [ ] La App `library` está creada.
- [ ] `library` está registrada en `INSTALLED_APPS`.
- [ ] El listado de libros funciona.
- [ ] Aparecen los 5 libros iniciales.
- [ ] Se muestra la disponibilidad.
- [ ] El formulario funciona.
- [ ] Los campos obligatorios se validan.
- [ ] Se puede registrar un nuevo libro.
- [ ] El nuevo libro aparece en el listado.
- [ ] No existen errores en la consola.
- [ ] `requirements.txt` está actualizado.
- [ ] `README.md` está actualizado.

---

# Comandos de Git y GitHub

Desde la raíz del repositorio:

```powershell
git status
```

Agregar los archivos modificados:

```powershell
git add .
```

Crear el commit:

```powershell
git commit -m "Implementar app library del laboratorio 2"
```

Subir los cambios:

```powershell
git push
```

Si estás trabajando específicamente en la rama `SIN-IA`:

```powershell
git push origin SIN-IA
```

---

# PROMPT PARA GITHUB COPILOT

El siguiente prompt puede utilizarse en Visual Studio Code con GitHub Copilot para ayudar a implementar el laboratorio.

```text
Quiero implementar el Laboratorio 02 de Desarrollo de Aplicaciones Empresariales en mi proyecto Django existente.

La problemática seleccionada es una biblioteca.

PROBLEMÁTICA:

En una biblioteca, los usuarios pueden perder tiempo buscando un libro en los estantes sin saber si se encuentra disponible. Esto puede generar molestias cuando finalmente descubren que el libro ya fue prestado. La aplicación permitirá consultar los libros y conocer su disponibilidad antes de buscarlos físicamente. El sistema será utilizado por los usuarios y el personal encargado de la biblioteca.

OBJETIVO:

Crear una nueva App Django llamada "library" que permita gestionar información de libros utilizando datos estáticos en memoria y formularios Django.

REGLAS IMPORTANTES:

1. Utilizar Python 3.10 o superior.
2. Utilizar Django 5.
3. No utilizar una base de datos para los libros.
4. No crear migraciones para los libros.
5. No utilizar ModelForm.
6. Utilizar forms.Form.
7. Guardar los libros como una lista de diccionarios en library/models.py.
8. Crear como mínimo 5 libros de ejemplo.
9. Utilizar el patrón MVT de Django.
10. La nueva App library debe convivir con la App core existente.
11. No modificar innecesariamente la App core.
12. Utilizar templates que hereden de base.html si el proyecto existente ya utiliza ese template.
13. Los registros creados mediante el formulario se deben guardar solamente en memoria.
14. Los datos agregados se perderán al reiniciar el servidor. Esto es esperado y debe quedar documentado.

ENTIDAD PRINCIPAL:

Libro

Campos:

- id: entero, obligatorio.
- titulo: texto, obligatorio.
- autor: texto, obligatorio.
- categoria: texto, obligatorio.
- disponible: booleano.

REQUISITOS FUNCIONALES:

RF01 — El sistema debe permitir visualizar el listado de libros.

RF02 — El sistema debe permitir conocer si un libro está disponible o prestado.

RF03 — El sistema debe permitir registrar un nuevo libro.

RF04 — El sistema debe validar los campos obligatorios.

RF05 — El sistema debe mostrar el nuevo libro después de registrarlo correctamente.

RF06 — El sistema debe permitir buscar un libro por título.

RF07 — El sistema debe permitir buscar por autor.

RF08 — El sistema debe permitir filtrar por categoría.

RF09 — El sistema debe permitir visualizar información principal del libro.

RF10 — El sistema debe permitir actualizar la disponibilidad.

RF11 — El sistema debe permitir editar la información del libro.

RF12 — El sistema debe permitir eliminar un libro.

ESTRUCTURA ESPERADA:

src/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
├── core/
│   └── ...
└── library/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        └── library/
            ├── lista.html
            └── crear.html

IMPLEMENTACIÓN INICIAL:

Primero implementa correctamente:

1. library/models.py con al menos 5 libros.
2. library/forms.py usando forms.Form.
3. library/views.py.
4. library/urls.py.
5. Template para listar libros.
6. Template para registrar libros.
7. Integración de library en config/settings.py.
8. Integración de library en config/urls.py.
9. Listado de libros.
10. Registro de nuevos libros.
11. Validación del formulario.
12. Redirección al listado después de registrar.

ANTES DE MODIFICAR ARCHIVOS:

Revisa la estructura actual del proyecto y verifica cómo están organizados config y core.

Adapta las rutas a la estructura existente.

NO sobrescribas archivos importantes sin revisar primero su contenido.

Después de implementar, verifica que:

- python manage.py check no tenga errores.
- El servidor pueda iniciarse con python manage.py runserver.
- /library/ muestre los libros.
- /library/crear/ muestre el formulario.
- El formulario permita registrar un libro.
- El nuevo libro aparezca en el listado.
- Los datos sean almacenados únicamente en memoria.

Al finalizar, indícame:

1. Qué archivos creaste.
2. Qué archivos modificaste.
3. Qué código implementaste.
4. Cómo ejecutar el proyecto.
5. Cómo probar el listado.
6. Cómo probar el formulario.
7. Qué limitaciones tiene el almacenamiento en memoria.
```

---

# CONCLUSIÓN

El laboratorio permite desarrollar una aplicación web utilizando Django y el patrón MVT a partir de una problemática real. En este caso se seleccionó la problemática de una biblioteca, donde los usuarios necesitan consultar los libros y conocer su disponibilidad antes de buscarlos físicamente.

A partir de esta problemática se definieron los requisitos funcionales y la entidad principal `Libro`, cuyos datos serán manejados mediante una lista de diccionarios en memoria. Posteriormente se implementará la nueva App `library`, integrada al proyecto existente y conectada con `core`.

La aplicación permitirá visualizar los libros y registrar nuevos ejemplares mediante un formulario construido con `forms.Form`. El flujo completo seguirá la estructura Request → URL → View → Model → Template → Response.

Finalmente, se verificará el funcionamiento de la aplicación y se actualizará el repositorio de GitHub con el código fuente, `requirements.txt`, `README.md` y las evidencias correspondientes.

> **Limitación:** debido a que el laboratorio no utiliza una base de datos, los registros agregados durante la ejecución se perderán cuando se reinicie el servidor.

---

# IMPLEMENTACIÓN COMPLETADA

## Resumen de la Implementación

Se ha completado la implementación del Laboratorio 02 con **todas las funcionalidades requeridas** en una aplicación Django funcional.

### Ejercicio 1 — Investigación de la Problemática ✓

La problemática fue documentada al inicio de este archivo:
- **Contexto:** Usuarios de biblioteca pierden tiempo buscando libros sin conocer disponibilidad
- **Solución:** Aplicación web que permite consultar libros y conocer su estado

### Ejercicio 2 — Requisitos Funcionales ✓

Se implementaron **12 requisitos funcionales (RF01-RF12)**:
- RF01: Consultar listado de libros ✓
- RF02: Ver disponibilidad (Disponible/Prestado) ✓
- RF03: Registrar nuevos libros ✓
- RF04: Validar datos obligatorios ✓
- RF05: Mostrar nuevo libro en listado ✓
- RF06: Buscar por título ✓
- RF07: Buscar por autor ✓
- RF08: Filtrar por categoría ✓
- RF09: Ver información detallada del libro ✓
- RF10: Actualizar disponibilidad ✓
- RF11: Editar información del libro ✓
- RF12: Eliminar libros ✓

### Ejercicio 3 — Modelo de Datos ✓

Se definió la entidad `Libro` con campos:
- `id`: Entero único
- `titulo`: Texto obligatorio
- `autor`: Texto obligatorio
- `categoria`: Texto obligatorio
- `disponible`: Booleano (True/False)

### Ejercicio 4 — Crear la App ✓

Se creó la app `library` registrada en `config/settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'core',
    'library',
]
```

### Ejercicio 5 — Datos Estáticos ✓

Se implementó `library/models.py` con una lista de **5 libros de ejemplo** almacenados en memoria:
- Cien años de soledad (Disponible)
- Don Quijote de la Mancha (Prestado)
- El principito (Disponible)
- 1984 (Disponible)
- Orgullo y prejuicio (Prestado)

### Ejercicio 6 — Listado ✓

Se implementó:
- **Vista:** `lista_libros()` en `library/views.py`
- **URL:** `/library/` en `library/urls.py`
- **Template:** `library/templates/library/lista.html`
- **Características:** Muestra tabla con ID, Título, Autor, Categoría, Disponibilidad

### Ejercicio 7 — Formulario ✓

Se creó `library/forms.py` con `LibroForm` usando `forms.Form`:
- Campo: `titulo` (CharField, max_length=200, obligatorio)
- Campo: `autor` (CharField, max_length=150, obligatorio)
- Campo: `categoria` (CharField, max_length=100, obligatorio)
- Campo: `disponible` (BooleanField, opcional)

### Ejercicio 8 — Crear Libro ✓

Se implementó:
- **Vista:** `crear_libro()` con GET (mostrar form) y POST (procesar)
- **Validación:** Django valida automáticamente los campos
- **Redirección:** Después de crear, redirige a `/library/`
- **Template:** `library/templates/library/crear.html`

### Ejercicio 9 — Funcionalidades Adicionales ✓

Se implementaron todas las funcionalidades extras:

#### Buscar por Título (RF06)
- Campo de texto en el listado
- Búsqueda case-insensitive
- Filtra resultados en tiempo real

#### Buscar por Autor (RF07)
- Campo de texto en el listado
- Búsqueda case-insensitive
- Funciona en combinación con otros filtros

#### Filtrar por Categoría (RF08)
- Dropdown con todas las categorías
- Extrae automáticamente categorías únicas
- Permite filtrar el listado

#### Ver Información Detallada (RF09)
- **Vista:** `detalle_libro()` 
- **URL:** `/library/<id>/`
- **Template:** `library/templates/library/detalle.html`
- Muestra: ID, Título, Autor, Categoría, Disponibilidad

#### Actualizar Disponibilidad (RF10)
- **Vista:** `actualizar_disponibilidad()`
- **URL:** `/library/<id>/disponibilidad/`
- Cambia entre Disponible ↔ Prestado
- Modifica directamente en la lista en memoria

#### Editar Libro (RF11)
- **Vista:** `editar_libro()`
- **URL:** `/library/<id>/editar/`
- **Template:** `library/templates/library/editar.html`
- Pre-llena el formulario con datos actuales
- Valida cambios antes de guardar

#### Eliminar Libro (RF12)
- **Vista:** `eliminar_libro()`
- **URL:** `/library/<id>/eliminar/`
- **Template:** `library/templates/library/eliminar.html`
- Pide confirmación antes de eliminar
- Elimina de la lista en memoria

### Ejercicio 10 — Archivos Finales ✓

#### Archivos Creados
1. `library/models.py` — Datos estáticos (lista de libros)
2. `library/forms.py` — Formulario LibroForm
3. `library/views.py` — 7 vistas principales
4. `library/urls.py` — Rutas de la app
5. `library/templates/library/lista.html` — Listado con búsqueda/filtro
6. `library/templates/library/crear.html` — Formulario crear
7. `library/templates/library/detalle.html` — Información del libro
8. `library/templates/library/editar.html` — Formulario editar
9. `library/templates/library/eliminar.html` — Confirmación eliminar
10. `library/templates/library/actualizar_disponibilidad.html` — Cambiar estado
11. `library/static/library/css/style.css` — Estilos personalizados

#### Archivos Modificados
1. `config/settings.py` — Agregada app 'library' a INSTALLED_APPS
2. `config/urls.py` — Agregada ruta `path('library/', include('library.urls'))`

## Estructura del Proyecto

```
src/
├── manage.py
├── config/
│   ├── settings.py (MODIFICADO)
│   ├── urls.py (MODIFICADO)
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── base.html
│   ├── static/
│   │   └── core/css/style.css
│   └── ...
└── library/ (NUEVO)
    ├── migrations/
    ├── models.py (NUEVO)
    ├── forms.py (NUEVO)
    ├── views.py (NUEVO)
    ├── urls.py (NUEVO)
    ├── static/
    │   └── library/css/style.css (NUEVO)
    ├── templates/
    │   └── library/
    │       ├── lista.html (NUEVO)
    │       ├── crear.html (NUEVO)
    │       ├── detalle.html (NUEVO)
    │       ├── editar.html (NUEVO)
    │       ├── eliminar.html (NUEVO)
    │       └── actualizar_disponibilidad.html (NUEVO)
    └── ...
```

## Patrón MVT

La aplicación sigue el patrón MVT de Django:

```
REQUEST (Usuario accede a URL)
   ↓
URL ROUTING (config/urls.py → library/urls.py)
   ↓
VIEW (library/views.py - lógica de negocio)
   ↓
MODEL (library/models.py - datos en lista)
   ↓
TEMPLATE (library/templates/*.html - presentación)
   ↓
RESPONSE (HTML renderizado al navegador)
```

## Rutas Disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/library/` | GET | Listado de libros con búsqueda y filtros |
| `/library/crear/` | GET/POST | Formulario para crear nuevo libro |
| `/library/<id>/` | GET | Ver detalle de un libro |
| `/library/<id>/editar/` | GET/POST | Editar información de libro |
| `/library/<id>/eliminar/` | GET/POST | Eliminar libro |
| `/library/<id>/disponibilidad/` | GET/POST | Cambiar disponibilidad |

## Ejecución del Proyecto

### Instalación de Dependencias
```bash
pip install Django==5.2.17
```

### Ejecutar el Servidor
```bash
cd src
python manage.py runserver
```

El servidor iniciará en `http://127.0.0.1:8000/`

### Verificación
```bash
python manage.py check
```

## Pruebas Realizadas

✓ `/library/` — Listado de 5 libros inicial  
✓ Búsqueda por título funciona  
✓ Búsqueda por autor funciona  
✓ Filtro por categoría funciona  
✓ `/library/crear/` — Formulario se muestra  
✓ Registro de nuevo libro funciona  
✓ Nuevo libro aparece en listado  
✓ `/library/1/` — Detalle muestra información  
✓ Editar libro modifica datos  
✓ Cambiar disponibilidad funciona  
✓ Eliminar libro remueve de lista  
✓ Validación de formulario funciona  
✓ Errores se muestran correctamente  
✓ App core sigue funcionando  
✓ `python manage.py check` — Sin errores

## Limitaciones

⚠️ **Almacenamiento en Memoria**
- Los datos se almacenan en una lista de Python en memoria
- Al reiniciar el servidor, todos los datos se pierden
- Los cambios no persisten entre sesiones
- No es adecuado para producción

## Requisitos del Sistema

- Python 3.10+
- Django 5.2+
- Navegador web moderno
- Visual Studio Code (opcional)

## Notas de Implementación

1. **Sin Base de Datos:** Se usa una lista de diccionarios en memoria
2. **Sin Migraciones:** No se crearon migraciones para la app library
3. **Sin ModelForm:** Se utilizó `forms.Form` en lugar de `forms.ModelForm`
4. **Validación Django:** Validación automática de campos del formulario
5. **Reutilización de CSS:** Se creó CSS personalizado para library
6. **Convivencia con Core:** La app library coexiste sin afectar la app core existente

## Flujo de Uso

### 1. Ver Libros
1. Acceder a `/library/`
2. Ver tabla de libros con disponibilidad
3. Opcionalmente buscar o filtrar

### 2. Crear Libro
1. Clic en "Registrar nuevo libro"
2. Completar formulario
3. Enviar
4. Aparece en listado

### 3. Ver Detalles
1. Clic en "Ver" en listado o título en tabla
2. Visualizar información completa
3. Opciones: Editar, Cambiar disponibilidad, Eliminar

### 4. Editar Libro
1. Clic en "Editar"
2. Modificar datos
3. Guardar cambios
4. Retorna a detalle

### 5. Cambiar Disponibilidad
1. En detalle, clic en botón de disponibilidad
2. Confirmar cambio
3. Se actualiza inmediatamente

### 6. Eliminar Libro
1. Clic en "Eliminar"
2. Confirmar eliminación
3. Se remueve de lista

## Conclusión de la Implementación

Se completó exitosamente la implementación del Laboratorio 02 con:
- ✅ App completa y funcional
- ✅ Todos los 12 requisitos implementados
- ✅ Patrón MVT correctamente aplicado
- ✅ Datos en memoria como se requería
- ✅ Interfaz amigable y clara
- ✅ Validación de datos
- ✅ Integración con proyecto existente
- ✅ Sin errores en verificación Django

La aplicación está lista para uso y evaluación.
