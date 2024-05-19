from django.db import models

# Create your models here.

# Creando la tabla contabilidad_cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    rfc = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    importe = models.DecimalField(max_digits=8, decimal_places=2)
    pagada = models.BooleanField(default=False)
