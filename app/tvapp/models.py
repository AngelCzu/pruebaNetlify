from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sala(models.Model):
    nombreSala = models.CharField(max_length=100)  # Puedes ajustar la longitud máxima según tus necesidades

    def __str__(self):
        txt = "nombresala: {0}"
        return txt.format(self.nombreSala)

class Puntos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)