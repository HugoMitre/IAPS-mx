from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .utils import queryset_to_workbook
from personas.models import Persona
#from poms.models import cuestionarioPOMS
from analysis.models import factorPOMS
from encuestas.models import ImagenEncuesta
from django.db.models import StdDev, Avg


# Create your views here.
def index(request):



    #imagen20=ImagenEncuesta.objects.select_related().filter(imagenIAPS=20)
    #personasimg20= Persona.objects.select_related()
    #fpoms= factorPOMS.objects.extra(tables=['encuestas_imagenencuesta'],where=['encuestas_imagenencuesta.imagenIAPS=20', 'encuestas_imagenencuesta.persona_id=analysis_factorpoms.persona_id'])
    fpoms = factorPOMS.objects.filter(persona__imagenencuesta__imagenIAPS=20)

    coleram = fpoms.aggregate(Avg('colera'))['colera__avg']
    fatigam = fpoms.aggregate(Avg('fatiga'))['fatiga__avg']
    vigorm = fpoms.aggregate(Avg('vigor'))['vigor__avg']
    amistadm = fpoms.aggregate(Avg('amistad'))['amistad__avg']
    tensionm = fpoms.aggregate(Avg('tension'))['tension__avg']
    depresionm = fpoms.aggregate(Avg('deprimido'))['deprimido__avg']


    coleras = fpoms.aggregate(StdDev('colera'))['colera__stddev']
    fatigas = fpoms.aggregate(StdDev('fatiga'))['fatiga__stddev']
    vigors = fpoms.aggregate(StdDev('vigor'))['vigor__stddev']
    amistads = fpoms.aggregate(StdDev('amistad'))['amistad__stddev']
    tensions = fpoms.aggregate(StdDev('tension'))['tension__stddev']
    depresions = fpoms.aggregate(StdDev('deprimido'))['deprimido__stddev']


    #factor = factorPOMS.objects.filter()

    #todos los poms
    #pomsmodel = cuestionarioPOMS.objects.all()

    # If it's a HTTP POST, we're interested in processing form data.


    if request.method == 'POST':

        queryset = fpoms

        columns = (
            'amistad', 'tension'
            )
        workbook = queryset_to_workbook(queryset, columns)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export.xls"'
        workbook.save(response)

        return response


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