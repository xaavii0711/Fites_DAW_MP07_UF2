from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return self.matricula + ' - ' + self.marca + " " + self.model

class Reserva(models.Model):
    automovil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    # Otros campos relevantes para la reserva

    def __str__(self):
        return f"Reserva de {self.automovil} del {self.fecha_inicio} al {self.fecha_fin}"