"""
Datos estáticos de la biblioteca.

Los libros se almacenan en una lista de diccionarios en memoria.
No se utiliza una base de datos.
Los datos se pierden al reiniciar el servidor.
"""

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
