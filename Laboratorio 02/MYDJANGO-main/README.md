# Investigación y desarrollo de una nueva solución persistente

<<<<<<< HEAD
## Sistema Web de Gestión de Biblioteca
=======
## Información general

**Curso:** Desarrollo de Aplicaciones Empresariales <br>
**Integrantes:** Gonzalo Davila y Pedro Suarez  
**Laboratorio:** 02 — Clases, atributos y métodos  
**Tecnología:** Python 3.10+, Django 5, Visual Studio Code y GitHub  
**Problemática:** Consulta y registro de libros de una biblioteca.

> **Importante:** El laboratorio trabaja con datos estáticos en memoria. No se utilizará una base de datos, migraciones ni el panel de administración de Django. Los datos agregados mediante el formulario se perderán cuando se reinicie el servidor.
>>>>>>> b6f86ee48449f5387a38e981d18285ee5cb596f0

# PROGRAMA EN FUNCIONAMIENTO

<img width="1185" height="892" alt="image" src="https://github.com/user-attachments/assets/be6893c4-0092-4d24-a97d-3f6672e59f17" />

---

# EJERCICIO 7 — Investigar una problemática real

## 7.1 Problemática identificada

En una biblioteca, los usuarios pueden perder tiempo buscando un libro físicamente en los estantes sin saber si este se encuentra disponible. Esta situación genera molestias cuando el libro ya fue prestado o cuando existen varios ejemplares que no están correctamente registrados.

Además, el personal encargado necesita administrar información sobre libros, autores, categorías, usuarios y préstamos de manera organizada. Cuando esta información se maneja manualmente, pueden producirse errores en los registros, pérdida de información y dificultades para conocer rápidamente el estado de los libros.

Para solucionar esta problemática se propone desarrollar una **aplicación web empresarial para la gestión de una biblioteca**, que permita registrar, consultar, actualizar y eliminar información mediante una base de datos persistente en SQLite.

## 7.2 Usuarios involucrados

Los principales usuarios del sistema serán:

* **Personal de biblioteca:** encargado de registrar y administrar libros, autores, categorías y préstamos.
* **Usuarios de la biblioteca:** personas que necesitan consultar los libros disponibles y conocer su información.
* **Administrador:** responsable de mantener actualizada la información almacenada en el sistema.

## 7.3 Proceso que se desea mejorar

Actualmente, la consulta de disponibilidad puede requerir revisar físicamente los libros o utilizar registros manuales.

La aplicación permitirá centralizar esta información y realizar el proceso de manera digital:

```text
Usuario
   ↓
Consulta de libro
   ↓
Sistema Web
   ↓
Base de datos SQLite
   ↓
Información del libro
   ↓
Disponibilidad
```

De esta manera, el personal podrá administrar la información y los usuarios podrán consultar los libros de forma rápida.

## 7.4 Objetivo de la solución

Desarrollar una aplicación web utilizando **Django** que permita gestionar la información de una biblioteca mediante modelos relacionados, Django ORM, SQLite y operaciones CRUD.

La aplicación deberá permitir:

* Registrar información.
* Consultar registros.
* Actualizar información.
* Eliminar registros.
* Consultar relaciones entre entidades.
* Mantener la información almacenada de forma persistente.

---

# EJERCICIO 8 — Definir los requisitos funcionales

A partir de la problemática identificada se establecen los siguientes requisitos funcionales.

| Código | Requisito funcional                                                                      |
| ------ | ---------------------------------------------------------------------------------------- |
| RF01   | El sistema debe permitir registrar nuevos libros.                                        |
| RF02   | El sistema debe permitir listar todos los libros registrados.                            |
| RF03   | El sistema debe permitir consultar la información y disponibilidad de un libro.          |
| RF04   | El sistema debe permitir actualizar la información de un libro.                          |
| RF05   | El sistema debe permitir eliminar un libro registrado.                                   |
| RF06   | El sistema debe permitir registrar autores.                                              |
| RF07   | El sistema debe permitir registrar categorías para clasificar los libros.                |
| RF08   | El sistema debe permitir registrar usuarios de la biblioteca.                            |
| RF09   | El sistema debe permitir registrar préstamos asociados a libros y usuarios.              |
| RF10   | El sistema debe permitir actualizar y eliminar registros de las entidades administradas. |
| RF11   | El sistema debe permitir consultar los préstamos registrados.                            |
| RF12   | El sistema debe mostrar los datos almacenados utilizando Django ORM y SQLite.            |

## Justificación

Los requisitos fueron definidos considerando las principales necesidades de la biblioteca. Los requisitos RF01, RF04 y RF05 permiten implementar las operaciones **CREATE, UPDATE y DELETE**, mientras que RF02, RF03 y RF11 permiten implementar operaciones de **READ**.

Los demás requisitos permiten administrar diferentes tipos de información y justifican la utilización de múltiples entidades dentro de una base de datos relacional.

---

# EJERCICIO 9 — Diseñar el modelo de datos

Para solucionar la problemática se diseñaron cinco entidades principales:

1. Libro
2. Autor
3. Categoría
4. Usuario
5. Préstamo

Se utilizarán relaciones mediante `ForeignKey` para representar la relación entre los libros, autores y préstamos.

## 9.1 Entidad Libro

| Campo            | Tipo de dato | Clave |
| ---------------- | ------------ | ----- |
| id               | Integer      | PK    |
| titulo           | CharField    | —     |
| isbn             | CharField    | —     |
| anio_publicacion | Integer      | —     |
| disponible       | BooleanField | —     |
| autor            | ForeignKey   | FK    |

### Justificación

La entidad **Libro** es necesaria porque representa el recurso principal administrado por la biblioteca.

El campo `disponible` permite conocer si el libro puede ser solicitado por un usuario.

El campo `autor` permite relacionar cada libro con su autor correspondiente.

---

## 9.2 Entidad Autor

| Campo        | Tipo de dato | Clave |
| ------------ | ------------ | ----- |
| id           | Integer      | PK    |
| nombre       | CharField    | —     |
| apellido     | CharField    | —     |
| nacionalidad | CharField    | —     |

### Justificación

La entidad **Autor** permite almacenar información independiente de los autores de los libros.

Separar esta información en una entidad propia evita repetir los datos del autor en cada registro de libro y permite administrar los autores de manera independiente.

---

## 9.3 Entidad Categoría

| Campo       | Tipo de dato | Clave |
| ----------- | ------------ | ----- |
| id          | Integer      | PK    |
| nombre      | CharField    | —     |
| descripcion | TextField    | —     |

### Justificación

La entidad **Categoría** permite clasificar los libros según su temática, por ejemplo:

* Programación
* Matemática
* Literatura
* Ciencias
* Historia

Esto facilita posteriormente realizar búsquedas y filtros.

---

## 9.4 Entidad Usuario

| Campo    | Tipo de dato | Clave |
| -------- | ------------ | ----- |
| id       | Integer      | PK    |
| nombre   | CharField    | —     |
| apellido | CharField    | —     |
| correo   | EmailField   | —     |
| telefono | CharField    | —     |

### Justificación

La entidad **Usuario** permite registrar a las personas que utilizan los servicios de la biblioteca.

Su información es necesaria para identificar quién realiza un préstamo.

---

## 9.5 Entidad Préstamo

| Campo            | Tipo de dato | Clave |
| ---------------- | ------------ | ----- |
| id               | Integer      | PK    |
| fecha_prestamo   | DateField    | —     |
| fecha_devolucion | DateField    | —     |
| estado           | CharField    | —     |
| libro            | ForeignKey   | FK    |
| usuario          | ForeignKey   | FK    |

### Justificación

La entidad **Préstamo** registra las operaciones realizadas por los usuarios de la biblioteca.

Permite conocer:

* Qué libro fue prestado.
* Qué usuario realizó el préstamo.
* Cuándo se realizó.
* Cuándo debe devolverse.
* Cuál es el estado del préstamo.

La relación mediante `ForeignKey` permite asociar un préstamo con un libro y un usuario.

---

# 9.6 Relaciones entre entidades

La relación principal del sistema será:

```text
AUTOR
  │
  │ 1
  │
  │ N
  ↓
LIBRO
  │
  │ 1
  │
  │ N
  ↓
PRÉSTAMO
  ↑
  │ N
  │
  │ 1
USUARIO
```

La relación puede interpretarse de la siguiente manera:

* Un **Autor** puede tener varios **Libros**.
* Cada **Libro** pertenece a un **Autor**.
* Un **Libro** puede aparecer en varios registros de **Préstamo** a lo largo del tiempo.
* Un **Usuario** puede realizar varios **Préstamos**.
* Cada **Préstamo** pertenece a un **Usuario** y a un **Libro**.

La entidad **Categoría** se mantiene como una entidad independiente para cumplir con la administración de diferentes tipos de información y posteriormente puede ser relacionada con `Libro` mediante otra `ForeignKey`.

---

# EJERCICIO 10 — Representar las relaciones

## 10.1 Diagrama conceptual

```text
┌───────────────────┐
│      AUTOR        │
├───────────────────┤
│ PK id             │
│ nombre            │
│ apellido          │
│ nacionalidad      │
└─────────┬─────────┘
          │
          │ 1
          │
          │ N
          ▼
┌───────────────────┐
│      LIBRO        │
├───────────────────┤
│ PK id             │
│ titulo            │
│ isbn              │
│ anio_publicacion  │
│ disponible        │
│ FK autor_id       │
└─────────┬─────────┘
          │
          │ 1
          │
          │ N
          ▼
┌───────────────────┐
│     PRÉSTAMO      │
├───────────────────┤
│ PK id             │
│ fecha_prestamo    │
│ fecha_devolucion  │
│ estado            │
│ FK libro_id       │
│ FK usuario_id     │
└─────────┬─────────┘
          │
          │ N
          │
          │ 1
          ▼
┌───────────────────┐
│     USUARIO       │
├───────────────────┤
│ PK id             │
│ nombre            │
│ apellido          │
│ correo             │
│ telefono          │
└───────────────────┘


┌───────────────────┐
│    CATEGORÍA      │
├───────────────────┤
│ PK id             │
│ nombre            │
│ descripcion       │
└───────────────────┘
```

## 10.2 Justificación del modelo

El modelo permite separar la información en diferentes entidades, evitando almacenar todos los datos en una única tabla.

Las relaciones mediante `ForeignKey` permiten representar dependencias reales del sistema.

Por ejemplo, un autor puede tener múltiples libros, mientras que un préstamo necesita conocer tanto el libro prestado como el usuario que realizó el préstamo.

Esto permite utilizar las ventajas de una base de datos relacional y facilita las consultas mediante Django ORM.

---

# EJERCICIO 11 — Crear la aplicación Django

Se creará una nueva aplicación Django denominada:

```text
biblioteca
```

La estructura general del proyecto será:

```text
django_project/
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
│   └── biblioteca/
│       ├── migrations/
│       ├── templates/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       └── urls.py
│
├── requirements.txt
└── README.md
```

La aplicación deberá registrarse en `INSTALLED_APPS` dentro de `settings.py`.

```python
INSTALLED_APPS = [
    # Aplicaciones de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicación del proyecto
    'biblioteca',
]
```

También se configurarán las URLs principales del proyecto para incluir las URLs de la aplicación.

---

# EJERCICIO 12 — Implementar los Models

Los modelos serán implementados utilizando Django ORM.

Ejemplo conceptual:

```python
from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    anio_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='libros'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='libros'
    )

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    estado = models.CharField(max_length=30)

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    def __str__(self):
        return f"{self.libro} - {self.usuario}"
```

## Justificación

Los modelos representan las entidades definidas durante el diseño de la base de datos.

Django se encargará de convertir estos modelos en tablas de SQLite mediante las migraciones.

Las relaciones `ForeignKey` permiten establecer relaciones entre las tablas sin necesidad de administrar manualmente las claves foráneas.

---

# EJERCICIO 13 — Crear la base de datos mediante migraciones

Después de implementar los modelos se ejecutarán las migraciones.

Desde la carpeta donde se encuentra `manage.py`:

```bash
python manage.py makemigrations
```

Después:

```bash
python manage.py migrate
```

Finalmente se verificará el estado de las migraciones mediante:

```bash
python manage.py showmigrations
```

## Evidencia requerida

Se deberá realizar una captura de pantalla donde se observe:

* Ejecución de `makemigrations`.
* Ejecución de `migrate`.
* Migraciones aplicadas correctamente.
* Resultado de `showmigrations`.

### Captura 13.1 — Migraciones ejecutadas

**Captura:** Terminal de Visual Studio Code mostrando las migraciones realizadas correctamente.

**Explicación:**

Las migraciones permiten crear y modificar la estructura de la base de datos SQLite a partir de los modelos definidos en Django.

---

# EJERCICIO 14 — Implementar CREATE

La aplicación deberá permitir registrar nuevos datos mediante formularios HTML y peticiones `POST`.

El flujo será:

```text
Formulario
    ↓
POST
    ↓
View
    ↓
Django ORM
    ↓
INSERT
    ↓
SQLite
    ↓
redirect
    ↓
Listado
```

Por ejemplo, para registrar un libro se utilizará una vista que reciba los datos enviados por el formulario y cree un nuevo objeto mediante Django ORM.

Conceptualmente:

```python
if request.method == "POST":
    Libro.objects.create(
        titulo=request.POST["titulo"],
        isbn=request.POST["isbn"],
        anio_publicacion=request.POST["anio_publicacion"],
        disponible=True,
        autor_id=request.POST["autor"]
    )

    return redirect("lista_libros")
```

## Evidencia requerida

**Captura 14.1 — Formulario de registro**

Debe mostrar el formulario utilizado para registrar información.

**Captura 14.2 — Registro creado**

Debe mostrar el listado después de guardar el nuevo registro.

## Caso de prueba

**Entrada:** Datos válidos de un libro.

**Resultado esperado:** El libro es almacenado en SQLite y posteriormente aparece en el listado.

---

# EJERCICIO 15 — Implementar READ

La aplicación deberá mostrar los registros almacenados en SQLite utilizando Django ORM.

Ejemplo:

```python
libros = Libro.objects.all()
```

También podrán utilizarse filtros y ordenamientos:

```python
libros = Libro.objects.filter(disponible=True)
```

```python
libros = Libro.objects.order_by("titulo")
```

La información será enviada desde la View hacia un Template.

Flujo:

```text
SQLite
   ↓
Django ORM
   ↓
QuerySet
   ↓
View
   ↓
Template
   ↓
HTML
```

## Pantallas esperadas

La aplicación deberá contar con listados para las entidades principales:

* Lista de libros.
* Lista de autores.
* Lista de categorías.
* Lista de usuarios.
* Lista de préstamos.

## Caso de prueba

**Entrada:** Acceder al listado de libros.

**Resultado esperado:** El sistema consulta SQLite mediante Django ORM y muestra los libros registrados.

---

# EJERCICIO 16 — Implementar UPDATE

Cada registro deberá disponer de una opción para modificar sus datos.

El flujo será:

```text
Seleccionar registro
        ↓
GET
        ↓
Formulario con datos actuales
        ↓
POST
        ↓
Modificar objeto
        ↓
save()
        ↓
Django ORM
        ↓
UPDATE
        ↓
SQLite
        ↓
redirect
        ↓
Listado actualizado
```

Ejemplo conceptual:

```python
libro = Libro.objects.get(id=libro_id)

if request.method == "POST":
    libro.titulo = request.POST["titulo"]
    libro.isbn = request.POST["isbn"]
    libro.anio_publicacion = request.POST["anio_publicacion"]

    libro.save()

    return redirect("lista_libros")
```

## Evidencia requerida

**Captura 16.1 — Formulario de actualización**

Debe mostrar los datos actuales del registro.

**Captura 16.2 — Registro actualizado**

Debe mostrar el listado después de guardar los cambios.

## Caso de prueba

**Entrada:** Modificar el título de un libro.

**Resultado esperado:** El nuevo título se almacena correctamente en SQLite y aparece actualizado en el listado.

---

# EJERCICIO 17 — Implementar DELETE

Cada registro deberá disponer de una opción para eliminarlo.

Antes de eliminar el registro se deberá mostrar una pantalla de confirmación.

El proceso será:

```text
Seleccionar registro
        ↓
Confirmación
        ↓
POST
        ↓
delete()
        ↓
Django ORM
        ↓
DELETE
        ↓
SQLite
        ↓
redirect
        ↓
Listado actualizado
```

Ejemplo conceptual:

```python
libro = Libro.objects.get(id=libro_id)

if request.method == "POST":
    libro.delete()
    return redirect("lista_libros")
```

La eliminación deberá realizarse mediante `POST` y no mediante un enlace GET directo.

## Evidencia requerida

**Captura 17.1 — Confirmación de eliminación**

Debe mostrar el registro que será eliminado y un botón para confirmar.

**Captura 17.2 — Registro eliminado**

Debe mostrar el listado después de realizar la eliminación.

## Caso de prueba

**Entrada:** Confirmar la eliminación de un libro.

**Resultado esperado:** El registro desaparece del listado y deja de existir en SQLite.

---

# PUBLICACIÓN EN GITHUB

Una vez finalizada la implementación, se deberán actualizar los archivos:

```text
README.md
requirements.txt
```

El archivo `README.md` debe contener:

* Problemática.
* Usuarios involucrados.
* Requisitos funcionales.
* Entidades.
* Campos.
* Relaciones.
* Diagrama.
* Explicación de la aplicación.
* Evidencias de funcionamiento.
* Casos de prueba.

El archivo `requirements.txt` debe contener las dependencias utilizadas por el proyecto.

Por ejemplo:

```text
Django==5.0.0
```

> La versión debe corresponder con la versión de Django instalada en el entorno virtual del proyecto.

---

# COMANDOS UTILIZADOS

## Activar entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Ejecutar servidor

```bash
python manage.py runserver
```

## Crear migraciones

```bash
python manage.py makemigrations
```

## Aplicar migraciones

```bash
python manage.py migrate
```

## Verificar migraciones

```bash
python manage.py showmigrations
```

---

# GIT Y GITHUB

Después de finalizar los cambios:

```bash
git status
```

Agregar los archivos:

```bash
git add .
```

Crear el commit:

```bash
git commit -m "Implementar sistema de gestion de biblioteca"
```

Subir los cambios:

```bash
git push
```

Finalmente verificar que los archivos y cambios aparezcan correctamente en el repositorio de GitHub.

---

# ESTRUCTURA DE EVIDENCIAS

Cada ejercicio deberá presentar su respectiva evidencia siguiendo el formato solicitado.

## Ejercicio 7

### Captura 7.1 — Problemática identificada

**Título:** Problemática real de la biblioteca.

**Captura:** Sección del `README.md` donde se describe la problemática, usuarios y proceso que se desea mejorar.

**Explicación:** Se presenta el problema real identificado y se justifica la necesidad de desarrollar una aplicación web.

---

## Ejercicio 8

### Captura 8.1 — Requisitos funcionales

**Título:** Requisitos funcionales del sistema.

**Captura:** Tabla de RF01 a RF12.

**Explicación:** Los requisitos representan las funciones principales que deberá realizar la aplicación.

---

## Ejercicio 9

### Captura 9.1 — Modelo de datos

**Título:** Entidades y campos.

**Captura:** Tabla de las cinco entidades y sus respectivos campos.

**Explicación:** Se muestran las entidades utilizadas para representar la información de la biblioteca.

---

## Ejercicio 10

### Captura 10.1 — Diagrama de relaciones

**Título:** Modelo relacional de la biblioteca.

**Captura:** Diagrama donde se observan las entidades y relaciones mediante ForeignKey.

**Explicación:** El diagrama representa cómo se relacionan las entidades dentro de la base de datos.

---

## Ejercicio 11

### Captura 11.1 — Aplicación Django

**Título:** App biblioteca creada y registrada.

**Captura:** Estructura del proyecto y `INSTALLED_APPS`.

**Explicación:** Se evidencia la creación de la aplicación y su integración con el proyecto Django.

---

## Ejercicio 12

### Captura 12.1 — Django Models

**Título:** Modelos implementados.

**Captura:** Archivo `models.py`.

**Explicación:** Los modelos representan las entidades diseñadas y contienen las relaciones `ForeignKey`.

---

## Ejercicio 13

### Captura 13.1 — Migraciones

**Título:** Base de datos creada mediante migraciones.

**Captura:** Terminal con `makemigrations`, `migrate` y `showmigrations`.

**Explicación:** Las migraciones permiten generar la estructura persistente en SQLite.

---

## Ejercicio 14

### Captura 14.1 — CREATE

**Título:** Registro de información.

**Captura:** Formulario y resultado después de guardar.

**Explicación:** Se evidencia la creación de un registro mediante POST y Django ORM.

---

## Ejercicio 15

### Captura 15.1 — READ

**Título:** Listado de información.

**Captura:** Pantalla mostrando los registros almacenados.

**Explicación:** Los datos son obtenidos desde SQLite mediante QuerySets y mostrados mediante Templates.

---

## Ejercicio 16

### Captura 16.1 — UPDATE

**Título:** Actualización de información.

**Captura:** Formulario con datos actuales y resultado actualizado.

**Explicación:** El sistema recupera el objeto, modifica sus propiedades y utiliza `save()` para actualizarlo.

---

## Ejercicio 17

### Captura 17.1 — DELETE

**Título:** Eliminación de información.

**Captura:** Pantalla de confirmación y listado después de eliminar.

**Explicación:** La aplicación solicita confirmación y realiza la eliminación mediante una petición POST y `delete()`.

---

# CASOS DE PRUEBA

| Código | Operación | Acción                            | Resultado esperado                             |
| ------ | --------- | --------------------------------- | ---------------------------------------------- |
| CP01   | CREATE    | Registrar un libro                | El libro aparece en el listado.                |
| CP02   | READ      | Consultar libros                  | Se muestran los libros almacenados.            |
| CP03   | READ      | Filtrar libros disponibles        | Se muestran únicamente libros disponibles.     |
| CP04   | UPDATE    | Modificar información de un libro | Los nuevos datos aparecen correctamente.       |
| CP05   | DELETE    | Eliminar un libro                 | El libro desaparece del listado.               |
| CP06   | CREATE    | Registrar un usuario              | El usuario queda almacenado.                   |
| CP07   | CREATE    | Registrar un préstamo             | El préstamo queda asociado al libro y usuario. |
| CP08   | READ      | Consultar préstamos               | Se muestran los préstamos registrados.         |

---

# CONCLUSIONES

## Conclusión 1

El desarrollo del sistema de gestión de biblioteca permite aplicar los principales conceptos de Django para construir una aplicación empresarial persistente. La utilización de modelos, relaciones `ForeignKey`, Django ORM y SQLite permite organizar la información de manera estructurada y realizar operaciones CRUD de forma eficiente.

## Conclusión 2

La solución propuesta permite digitalizar un proceso real de una biblioteca, facilitando la administración de libros, autores, usuarios y préstamos. Además, el uso de relaciones entre entidades permite representar correctamente la información y establecer una base sólida para ampliar el sistema con nuevas funcionalidades en el futuro.

---

# TECNOLOGÍAS UTILIZADAS

* Python
* Django
* Django ORM
* SQLite
* HTML
* CSS
* JavaScript
* Visual Studio Code
* Git
* GitHub
* GitHub Copilot

---

# RESULTADO ESPERADO

Al finalizar el proyecto, la aplicación deberá permitir administrar la información de la biblioteca mediante una interfaz web y una base de datos SQLite.

El sistema deberá demostrar correctamente:

```text
CREATE
  ↓
READ
  ↓
UPDATE
  ↓
DELETE
```

<<<<<<< HEAD
utilizando Django ORM y manteniendo la información de manera persistente.
=======
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
>>>>>>> b6f86ee48449f5387a38e981d18285ee5cb596f0
