# Desarrollo de Aplicaciones Empresariales — Proyecto Django

## Introducción

Este documento presenta el desarrollo paso a paso de una aplicación web utilizando **Django 5**, **Python**, **Visual Studio Code** y **GitHub Copilot**.

El proyecto consiste en crear una aplicación denominada `core`, cuyo objetivo es administrar y mostrar una lista de elementos (`Item`) mediante una interfaz web y el panel de administración de Django.

Durante el desarrollo se evidencia cada etapa mediante comandos ejecutados en la terminal de Visual Studio Code, archivos de configuración, código fuente y capturas de pantalla.

---

# 1. Preparar el entorno de trabajo

## Objetivo

Crear la carpeta principal del proyecto, configurar un entorno virtual de Python y crear la carpeta `src/`, que contendrá el código fuente de la aplicación.

## Procedimiento

Desde la terminal de Visual Studio Code se crea la carpeta principal:

```bash
mkdir django_project
cd django_project
```

Posteriormente se crea el entorno virtual:

```bash
python -m venv venv
```

Para activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Una vez activado, la terminal debe mostrar el nombre del entorno virtual, por ejemplo:

```text
(venv) C:\...\django_project>
```

Finalmente se crea la carpeta `src`:

```bash
mkdir src
```

La estructura inicial queda:

```text
django_project/
├── venv/
└── src/
```

## Evidencia

**Captura 1 — Creación y activación del entorno virtual**

![Creación y activación del entorno virtual](docs/img/01-entorno-virtual.png)

> En esta captura se debe evidenciar la creación de `django_project`, el entorno virtual `venv`, su activación y la creación de `src/`.

---

# 2. Instalar Django

## Objetivo

Instalar Django versión 5 dentro del entorno virtual y comprobar que la instalación fue realizada correctamente.

Con el entorno virtual activado se ejecuta:

```bash
python -m pip install "Django>=5,<6"
```

Después se comprueba la versión instalada:

```bash
python -m django --version
```

El resultado debe corresponder a una versión de Django 5.x.

También se puede verificar mediante:

```bash
pip show django
```

## Evidencia

**Captura 2 — Instalación y verificación de Django**

![Instalación de Django](docs/img/02-instalacion-django.png)

> La captura debe mostrar la instalación mediante `pip` y el resultado de `python -m django --version`.

---

# 3. Crear el proyecto con configuración separada

## Objetivo

Crear el proyecto Django denominado `config` dentro de `src/`, manteniendo `manage.py` directamente en `src/` y los archivos de configuración dentro de `src/config/`.

Desde la carpeta raíz del proyecto se ejecuta:

```bash
django-admin startproject config src
```

La estructura resultante es:

```text
django_project/
├── venv/
└── src/
    ├── manage.py
    └── config/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

Esta estructura permite separar claramente el código fuente del entorno virtual y mantener la configuración del proyecto dentro de `config`.

## Evidencia

**Captura 3 — Creación del proyecto Django**

![Estructura del proyecto](docs/img/03-proyecto-django.png)

> La captura debe mostrar en el explorador de VS Code que `manage.py` se encuentra dentro de `src/` y que `settings.py`, `urls.py`, `asgi.py` y `wsgi.py` están dentro de `src/config/`.

---

# 4. Crear y registrar la aplicación core

## Objetivo

Crear una aplicación Django denominada `core` y registrarla dentro de `INSTALLED_APPS`.

Primero se ingresa a `src`:

```bash
cd src
```

Luego se crea la aplicación:

```bash
python manage.py startapp core
```

La estructura de la aplicación será similar a:

```text
src/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── core/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```

Después se abre:

```text
src/config/settings.py
```

y se agrega `core` a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "core",
]
```

## Evidencia

**Captura 4 — Aplicación core registrada**

![Aplicación core](docs/img/04-core-registrada.png)

> La captura debe mostrar la carpeta `core` y la modificación de `INSTALLED_APPS`.

---

# 5. Definir el modelo Item

## Objetivo

Crear el modelo `Item` con los campos:

* `name`: nombre del elemento.
* `description`: descripción opcional.
* `created_at`: fecha y hora de creación automática.

En:

```text
src/core/models.py
```

se define:

```python
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### Explicación

`CharField` permite almacenar texto de longitud limitada. En este caso, el nombre puede tener hasta 200 caracteres.

`TextField` permite almacenar texto más extenso. La opción `blank=True` permite que la descripción pueda quedar vacía.

`DateTimeField(auto_now_add=True)` registra automáticamente la fecha y hora en que se crea cada objeto.

El método `__str__()` permite que los objetos se muestren utilizando su nombre en el panel de administración.

## Generar las migraciones

Desde `src/`:

```bash
python manage.py makemigrations
```

Después se aplican:

```bash
python manage.py migrate
```

Las migraciones permiten convertir la definición del modelo Python en la estructura correspondiente de la base de datos.

## Evidencia

**Captura 5 — Modelo Item y migraciones**

![Modelo Item](docs/img/05-modelo-migraciones.png)

> La captura debe evidenciar el contenido de `models.py`, la ejecución de `makemigrations` y la ejecución de `migrate`.

---

# 6. Crear la vista y las URLs

## Objetivo

Crear una vista que consulte todos los objetos `Item` y los envíe a una plantilla HTML.

## Crear la vista

En:

```text
src/core/views.py
```

se escribe:

```python
from django.shortcuts import render

from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, "core/item_list.html", {"items": items})
```

La consulta:

```python
Item.objects.all()
```

obtiene todos los registros existentes del modelo `Item`.

La función `render()` combina la información obtenida con la plantilla HTML.

## Crear las URLs de core

Se crea:

```text
src/core/urls.py
```

con el siguiente contenido:

```python
from django.urls import path

from .views import item_list


urlpatterns = [
    path("", item_list, name="item_list"),
]
```

## Enlazar las URLs de la aplicación

En:

```text
src/config/urls.py
```

se configura:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
```

El uso de:

```python
include("core.urls")
```

permite que las URLs de la aplicación `core` sean incorporadas a las URLs principales del proyecto.

## Evidencia

**Captura 6 — Vista y configuración de URLs**

![Vista y URLs](docs/img/06-vista-urls.png)

> La captura debe mostrar `views.py`, `core/urls.py` y `config/urls.py`.

---

# 7. Crear las plantillas

## Objetivo

Crear una plantilla base reutilizable y una plantilla específica para mostrar los elementos almacenados.

Se recomienda crear la siguiente estructura:

```text
src/
└── core/
    └── templates/
        ├── base.html
        └── core/
            └── item_list.html
```

## Plantilla base

En:

```text
src/core/templates/base.html
```

se crea:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Items{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Gestión de Items</h1>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

## Plantilla item_list

En:

```text
src/core/templates/core/item_list.html
```

se crea:

```html
{% extends "base.html" %}

{% block title %}Lista de Items{% endblock %}

{% block content %}
    <h2>Lista de Items</h2>

    {% for item in items %}
        <article>
            <h3>{{ item.name }}</h3>

            {% if item.description %}
                <p>{{ item.description }}</p>
            {% endif %}

            <small>Creado: {{ item.created_at }}</small>
        </article>
    {% empty %}
        <p>No existen items registrados.</p>
    {% endfor %}
{% endblock %}
```

El bloque:

```django
{% for item in items %}
```

recorre todos los objetos enviados desde la vista.

El bloque:

```django
{% empty %}
```

permite mostrar un mensaje cuando no existen registros.

## Evidencia

**Captura 7 — Plantillas HTML**

![Plantillas](docs/img/07-plantillas.png)

> La captura debe mostrar `base.html`, `item_list.html` y la estructura de carpetas `templates`.

---

# 8. Configurar el administrador y cargar datos

## Objetivo

Registrar el modelo `Item` en el administrador de Django, crear un usuario administrador y utilizar el panel para ingresar datos.

## Registrar Item

En:

```text
src/core/admin.py
```

se configura:

```python
from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")
```

Esto permite visualizar el nombre y la fecha de creación en el listado del administrador.

## Crear el superusuario

Desde `src/`:

```bash
python manage.py createsuperuser
```

Django solicitará:

```text
Username:
Email address:
Password:
Password (again):
```

La contraseña no será visible mientras se escribe por motivos de seguridad.

## Ejecutar el servidor

```bash
python manage.py runserver
```

Luego se accede a:

```text
http://127.0.0.1:8000/admin/
```

Se inicia sesión utilizando las credenciales del superusuario.

## Registrar los elementos

Desde el panel:

1. Ingresar a **Items**.
2. Seleccionar **Add Item**.
3. Registrar el primer elemento.
4. Guardarlo.
5. Repetir el procedimiento para crear un segundo elemento.

Ejemplo:

| Name       | Description                |
| ---------- | -------------------------- |
| Producto 1 | Primer elemento de prueba  |
| Producto 2 | Segundo elemento de prueba |

## Evidencia

**Captura 8.1 — Registro del modelo en admin**

![Configuración del administrador](docs/img/08-admin-config.png)

**Captura 8.2 — Creación del superusuario**

![Superusuario](docs/img/08-superusuario.png)

**Captura 8.3 — Panel de administración**

![Panel de administración](docs/img/08-admin-panel.png)

**Captura 8.4 — Items registrados**

![Items registrados](docs/img/08-items.png)

> Las capturas deben evidenciar el registro del modelo, la creación del superusuario, el acceso al panel y la existencia de al menos dos elementos.

---

# 9. Verificar el funcionamiento

## Objetivo

Comprobar que la aplicación funciona correctamente tanto desde la página principal como desde el panel de administración.

Se ejecuta:

```bash
python manage.py runserver
```

Django mostrará una dirección similar a:

```text
Starting development server at http://127.0.0.1:8000/
```

## Página principal

Se accede a:

```text
http://127.0.0.1:8000/
```

La página debe mostrar los elementos registrados.

Por ejemplo:

```text
Gestión de Items

Lista de Items

Producto 1
Primer elemento de prueba

Producto 2
Segundo elemento de prueba
```

## Panel de administración

También se comprueba:

```text
http://127.0.0.1:8000/admin/
```

Debe aparecer el panel administrativo de Django y el modelo `Items`.

## Evidencia

**Captura 9.1 — Página principal funcionando**

![Página principal](docs/img/09-pagina-principal.png)

**Captura 9.2 — Panel de administración funcionando**

![Panel funcionando](docs/img/09-admin-funcionando.png)

> Las capturas deben demostrar que la aplicación funciona correctamente y que los datos registrados desde el administrador aparecen en la página principal.

---

# 10. Documentar y subir el proyecto

## 10.1 Generar requirements.txt

Con el entorno virtual activado se ejecuta:

```bash
pip freeze > requirements.txt
```

Este archivo permite conocer las dependencias necesarias para instalar el proyecto en otro equipo.

Se puede comprobar su contenido mediante:

```bash
type requirements.txt
```

En Linux/macOS:

```bash
cat requirements.txt
```

El archivo debe incluir Django y las demás dependencias instaladas.

---

## 10.2 Crear README.md

El presente documento funciona como documentación principal del proyecto.

Debe explicar:

* Objetivo del proyecto.
* Tecnologías utilizadas.
* Estructura de carpetas.
* Creación del entorno virtual.
* Instalación de dependencias.
* Aplicación de migraciones.
* Creación del superusuario.
* Ejecución del servidor.
* Acceso al sitio.
* Acceso al administrador.

---

## 10.3 Estructura final del proyecto

La estructura esperada es:

```text
django_project/
├── venv/
├── requirements.txt
├── README.md
├── .gitignore
└── src/
    ├── manage.py
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    └── core/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── ...
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        └── templates/
            ├── base.html
            └── core/
                └── item_list.html
```

---

## 10.4 Crear .gitignore

Antes de subir el proyecto a GitHub es importante evitar archivos innecesarios o sensibles.

Se crea:

```text
.gitignore
```

con:

```gitignore
venv/
__pycache__/
*.py[cod]
db.sqlite3
.env
.vscode/
```

El entorno virtual `venv/` no debe subirse al repositorio porque puede volver a crearse mediante `requirements.txt`.

---

## 10.5 Inicializar Git

Desde la carpeta raíz `django_project/`:

```bash
git init
```

Se agregan los archivos:

```bash
git add .
```

Se comprueba lo que será incluido:

```bash
git status
```

Después se crea el primer commit:

```bash
git commit -m "Crear proyecto Django con aplicación core"
```

---

## 10.6 Crear el repositorio en GitHub

En GitHub se crea un nuevo repositorio para el proyecto.

Una vez creado, se vincula el repositorio remoto con el proyecto local:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Se puede verificar:

```bash
git remote -v
```

Finalmente se suben los archivos:

```bash
git branch -M main
git push -u origin main
```

La URL exacta del repositorio debe reemplazarse por la correspondiente al repositorio creado.

## Evidencia

**Captura 10.1 — requirements.txt**

![Requirements](docs/img/10-requirements.png)

**Captura 10.2 — README.md y estructura final**

![Estructura final](docs/img/10-estructura-final.png)

**Captura 10.3 — Repositorio de GitHub**

![Repositorio GitHub](docs/img/10-github.png)

> La última captura debe mostrar el repositorio de GitHub con el proyecto correctamente subido.

---

# Uso de GitHub Copilot

Durante el desarrollo se utilizó **GitHub Copilot** como herramienta de asistencia para comprender y desarrollar el código.

Copilot puede ayudar a:

* Sugerir código Python.
* Explicar funciones y clases.
* Proponer estructuras de archivos.
* Detectar errores.
* Sugerir correcciones.
* Explicar conceptos de Django.

Sin embargo, las sugerencias deben ser revisadas y comprendidas antes de incorporarlas al proyecto. El objetivo no es copiar código automáticamente, sino utilizar la herramienta como apoyo durante el proceso de aprendizaje.

Por ejemplo, para comprender el modelo se puede solicitar a Copilot una explicación de:

```python
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

Posteriormente se debe verificar que la explicación coincida con el comportamiento real de Django.

---

# Comandos principales utilizados

A continuación se resumen los comandos utilizados durante el desarrollo:

```bash
mkdir django_project
cd django_project

python -m venv venv
venv\Scripts\activate

python -m pip install "Django>=5,<6"
python -m django --version

mkdir src
django-admin startproject config src

cd src
python manage.py startapp core

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Para preparar el proyecto para GitHub:

```bash
pip freeze > requirements.txt

git init
git add .
git commit -m "Crear proyecto Django con aplicación core"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

---

# Conclusiones

Se desarrolló una aplicación web básica utilizando Django 5, aplicando una estructura organizada mediante el directorio `src/` y el proyecto de configuración `config`.

Se creó la aplicación `core`, se definió el modelo `Item`, se generaron y aplicaron las migraciones, se implementó una vista para consultar los registros y se configuraron las URLs y plantillas.

También se configuró el administrador de Django, permitiendo crear y administrar elementos mediante un superusuario.

Finalmente, se verificó el funcionamiento de la aplicación desde el navegador, se generó `requirements.txt`, se documentó el proyecto mediante `README.md` y se preparó el código para su publicación en GitHub.

---

# Checklist de entrega

* [ ] Carpeta `django_project` creada.
* [ ] Entorno virtual `venv` creado y activado.
* [ ] Carpeta `src/` creada.
* [ ] Django 5 instalado.
* [ ] Versión de Django verificada.
* [ ] Proyecto `config` creado dentro de `src/`.
* [ ] Aplicación `core` creada.
* [ ] `core` registrado en `INSTALLED_APPS`.
* [ ] Modelo `Item` creado.
* [ ] Migraciones generadas y aplicadas.
* [ ] Vista `item_list` implementada.
* [ ] `core/urls.py` creado.
* [ ] `include()` configurado en `config/urls.py`.
* [ ] `base.html` creado.
* [ ] `core/item_list.html` creado.
* [ ] Modelo `Item` registrado en Django Admin.
* [ ] Superusuario creado.
* [ ] Al menos dos Items registrados.
* [ ] Página principal verificada.
* [ ] Panel `/admin/` verificado.
* [ ] `requirements.txt` generado.
* [ ] `.gitignore` creado.
* [ ] `README.md` creado.
* [ ] Proyecto subido a GitHub.
* [ ] Capturas de pantalla incorporadas a la documentación.
