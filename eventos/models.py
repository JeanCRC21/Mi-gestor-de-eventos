from django.core.exceptions import ValidationError
from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='')

    def clean(self):
        if Organizador.objects.filter(email=self.email).exists():
            raise ValidationError('Este correo ya está en uso.')

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"
