from django.db import models
from django.conf import settings


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre)


class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200, blank=True)
    imagen = models.CharField(max_length=125)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return str(self.nombre)
