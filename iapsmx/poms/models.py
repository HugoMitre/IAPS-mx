from django.db import models
from personas.models import Persona

# Create your models here.
class cuestionarioPOMS(models.Model):

    persona = models.OneToOneField(Persona)

    enfadado=models.IntegerField()
    agotado=models.IntegerField()
    llenoEnergia=models.IntegerField()
    amable = models.IntegerField()
    conNerviosPunta=models.IntegerField()
    infeliz=models.IntegerField()

    malhumorado=models.IntegerField()
    fatigado=models.IntegerField()
    energico=models.IntegerField()
    comprensivo=models.IntegerField()
    nervioso=models.IntegerField()
    triste=models.IntegerField()

    irritable=models.IntegerField()
    cansado=models.IntegerField()
    activo=models.IntegerField()
    servicial=models.IntegerField()
    tenso=models.IntegerField()
    desesperanzado=models.IntegerField()

    molesto=models.IntegerField()
    debil=models.IntegerField()
    animado=models.IntegerField()
    amistoso=models.IntegerField()
    agitado=models.IntegerField()
    solo=models.IntegerField()

    resentido=models.IntegerField()
    exhausto=models.IntegerField()
    vigoroso=models.IntegerField()
    consideradoConDemas=models.IntegerField()
    inquieto=models.IntegerField()
    melancolico=models.IntegerField()




