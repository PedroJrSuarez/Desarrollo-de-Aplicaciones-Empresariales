# Proyecto Django - Desarrollo de Aplicaciones Empresariales

## Descripción
Este proyecto es una aplicación web con Django 5 que gestiona una lista de elementos `Item` usando el panel administrativo de Django y una página principal con una vista personalizada.

## Tecnologías utilizadas
- Python
- Django 5
- SQLite
- Visual Studio Code
- GitHub Copilot

## Requisitos previos
- Python 3.10 o superior
- Entorno virtual de Python
- Git (opcional para versionado)

## Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

## Instalar dependencias
```bash
python -m pip install "Django>=5,<6"
```

## Estructura del proyecto
```text
django_project/
├── .gitignore
├── README.md
├── requirements.txt
├── venv/
└── src/
    ├── manage.py
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── core/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        └── templates/
            ├── base.html
            └── core/
                └── item_list.html
```

## Ejecutar migraciones
```bash
cd src
python manage.py migrate
```

## Crear superusuario
```bash
python manage.py createsuperuser
```

## Ejecutar el servidor
```bash
python manage.py runserver
```

## Acceso a la aplicación
- Página principal: http://127.0.0.1:8000/
- Administrador: http://127.0.0.1:8000/admin/

## Uso de GitHub Copilot
Se utilizó GitHub Copilot para apoyar la explicación, la generación de código y la validación del proyecto. Las sugerencias se revisaron y adaptaron para mantener coherencia con el proyecto.

## Comandos principales
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install "Django>=5,<6"
python -m django --version
python manage.py startapp core
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Clonar e instalar desde cero
```bash
git clone <url-del-repositorio>
cd django_project
venv\Scripts\activate
python -m pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Reto opcional

### 1. Estilos CSS
Se agregaron estilos propios en:
- `src/core/static/core/css/style.css`

Estos estilos mejoran la apariencia de la aplicación con:
- tipografía limpia
- encabezado institucional
- contenedor principal
- tarjetas de Items
- diseño responsive básico
- botones y elementos visualmente diferenciados

Se cargan desde la plantilla base mediante `{% load static %}` y la etiqueta:
```html
<link rel="stylesheet" href="{% static 'core/css/style.css' %}">
```

### 2. Interactividad con JavaScript vanilla
Se añadió un buscador en la plantilla principal que permite filtrar los Items sin recargar la página.

El campo de búsqueda es:
```html
<input type="search" id="item-search" placeholder="Buscar un item...">
```

El comportamiento se implementa en:
- `src/core/static/core/js/app.js`

Funcionalidad:
- escucha el texto escrito por el usuario
- compara nombre y descripción del Item
- oculta los elementos que no coinciden
- muestra un mensaje si no existen coincidencias

### 3. API JSON con Django
Se creó un endpoint para devolver todos los Items en formato JSON:
```text
/api/items/
```

La vista asociada devuelve un `JsonResponse` con los campos:
- `id`
- `name`
- `description`
- `created_at`

### 4. Consumo de la API con fetch()
La página principal también incluye una sección dinámica que consume la API con JavaScript vanilla y `fetch('/api/items/')`.

Esto permite mostrar los Items desde la API sin necesidad de recargar la página, y la sección refleja los datos actuales del sistema.

### 5. Cómo probar la API
Ejecuta el proyecto:
```bash
cd src
python manage.py runserver
```

Luego prueba estas URLs:
```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/items/
```

La URL de la API devuelve JSON como este ejemplo:
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "Equipo portátil",
    "created_at": "2026-08-19T20:00:00"
  }
]
```

### 6. Tecnologías utilizadas en el reto opcional
- HTML5
- CSS propio
- JavaScript vanilla
- Django nativo (`JsonResponse`)
- SQLite
- Fetch API para consumo de datos
