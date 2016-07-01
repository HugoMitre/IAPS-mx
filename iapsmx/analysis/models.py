from django.db import models
from personas.models import Persona
from poms.models import cuestionarioPOMS

# Create your models here.
class factorPOMS(models.Model):

    poms = models.OneToOneField(cuestionarioPOMS)
    persona = models.OneToOneField(Persona)

    colera = models.IntegerField()
    fatiga = models.IntegerField()
    vigor =models.IntegerField()
    amistad =models.IntegerField()
    tension=models.IntegerField()
    deprimido =models.IntegerField()