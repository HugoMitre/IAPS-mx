from django.db import models
from personas.models import Persona

# Create your models here.
class ImagenIAPS(models.Model):
    name = models.CharField(max_length=200)
    valence = models.DecimalField(max_digits=5, decimal_places=3)
    arousal = models.DecimalField(max_digits=5, decimal_places=3)
    neutral= models.CharField(max_length=200)
    tipo = models.BooleanField(default=False)


class ImagenEncuesta(models.Model):
    persona = models.ForeignKey(Persona)
    imagenIAPS =models.ForeignKey(ImagenIAPS)
    valencia = models.IntegerField()
    activacion = models.IntegerField()

    upset=models.IntegerField(null=True)
    stressed= models.IntegerField(null=True)
    nervous= models.IntegerField(null=True)
    tense= models.IntegerField(null=True)
    alert= models.IntegerField(null=True)
    excited= models.IntegerField(null=True)
    enthusiastic= models.IntegerField(null=True)
    elated= models.IntegerField(null=True)
    happy= models.IntegerField(null=True)
    contented= models.IntegerField(null=True)
    serene= models.IntegerField(null=True)
    relaxed= models.IntegerField(null=True)
    calm= models.IntegerField(null=True)
    bored= models.IntegerField(null=True)
    sluggish= models.IntegerField(null=True)
    depressed= models.IntegerField(null=True)
    sad= models.IntegerField(null=True)

    finished = models.BooleanField(default=False)


