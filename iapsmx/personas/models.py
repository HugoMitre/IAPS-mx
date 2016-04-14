from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):

    #user = models.OneToOneField(User)

    estado = models.IntegerField(default=32)
    edad = models.IntegerField(default=18)
    genero = models.IntegerField()


