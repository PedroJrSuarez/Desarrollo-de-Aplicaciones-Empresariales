from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Membresia(models.Model):
    tipo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo


class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dias_semana = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='rutinas')
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='rutinas')

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    observacion = models.TextField(blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='asistencias')

    def __str__(self):
        return f'{self.cliente} - {self.fecha}'
