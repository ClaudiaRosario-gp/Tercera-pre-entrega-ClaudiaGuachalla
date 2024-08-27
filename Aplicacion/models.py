from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Consultas(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_entrega = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
