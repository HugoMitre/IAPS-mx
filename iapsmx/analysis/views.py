from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from poms.models import cuestionarioPOMS
from analysis.models import factorPOMS

# Create your views here.
def index(request):
    coleram=0
    coleras=0

    fatigam=0
    fatigas=0

    vigorm=0
    vigors=0

    amistadm=0
    amistads=0

    tensionm=0
    tensions=0

    depresionm=0
    depresions=0

    #todos los poms
    #pomsmodel = cuestionarioPOMS.objects.all()

    # If it's a HTTP POST, we're interested in processing form data.


    if request.method == 'POST':
        """
        pomsmodel = cuestionarioPOMS.objects.all()
        # Attempt to grab information from the raw form information.

        #form = PomsForm(data=request.POST)

        ejecutar solo una vez

        for pomsx in pomsmodel:
            factorPOMS(poms = pomsx, persona = pomsx.persona, \
                      colera = pomsx.enfadado+pomsx.malhumorado+pomsx.irritable+pomsx.molesto+pomsx.resentido, \
                      fatiga = pomsx.agotado+pomsx.cansado+pomsx.fatigado+pomsx.debil+pomsx.exhausto, \
                      vigor = pomsx.llenoEnergia+pomsx.energico+pomsx.activo+pomsx.animado+pomsx.vigoroso,\
                      amistad = pomsx.amable+pomsx.comprensivo+pomsx.servicial+pomsx.consideradoConDemas+pomsx.amistoso,\
                      tension = pomsx.conNerviosPunta+pomsx.nervioso+pomsx.tenso+pomsx.agitado+pomsx.inquieto,\
                      deprimido = pomsx.infeliz+pomsx.triste+pomsx.desesperanzado+pomsx.solo+pomsx.melancolico
                      ).save()
        """


    return render(request, 'analysis/index.html', {'coleram':coleram, 'coleras':coleras, 'fatigam':fatigam, 'fatigas':fatigas, \
                                               'vigorm':vigorm, 'vigors':vigors, 'amistadm':amistadm, 'amistads':amistads, \
                                               'tensionm':tensionm, 'tensions':tensions,'depresionm':depresionm, 'depresions':depresions})