from django.shortcuts import render
from django.http import HttpResponse
from .utils import queryset_to_workbook
from analysis.models import factorPOMS
from encuestas.models import ImagenEncuesta
from django.db.models import StdDev, Avg


# Create your views here.
def index(request):



    #imagen20=ImagenEncuesta.objects.select_related().filter(imagenIAPS=20)
    #personasimg20= Persona.objects.select_related()
    #fpoms= factorPOMS.objects.extra(tables=['encuestas_imagenencuesta'],where=['encuestas_imagenencuesta.imagenIAPS=20', 'encuestas_imagenencuesta.persona_id=analysis_factorpoms.persona_id'])


    #factor = factorPOMS.objects.filter()

    #todos los poms
    #pomsmodel = cuestionarioPOMS.objects.all()

    # If it's a HTTP POST, we're interested in processing form data.

    n=60
    if request.method == 'POST':


        fpoms = factorPOMS.objects.filter(persona__imagenencuesta__imagenIAPS=n)

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

        filtrados =ImagenEncuesta.objects.filter(\
            imagenIAPS=n,
            persona__factorpoms__colera__range=(coleram-2*coleras, coleram+2*coleras),
            persona__factorpoms__fatiga__range=(fatigam-2*fatigas, fatigam+2*fatigas),
            persona__factorpoms__vigor__range=(vigorm-2*vigors, vigorm+2*vigors),
            persona__factorpoms__amistad__range=(amistadm-2*amistads, amistadm+2*amistads),
            persona__factorpoms__tension__range=(tensionm-2*tensions, tensionm+2*tensions),
            persona__factorpoms__deprimido__range=(depresionm-2*depresions, depresionm+2*depresions),
            )

        queryset = filtrados

        columns = (
            'persona_id',
            'imagenIAPS_id',
            'valencia',
            'activacion',
            'upset',
            'stressed',
            'nervous',
            'tense',
            'alert',
            'excited',
            'enthusiastic',
            'elated',
            'happy',
            'contented',
            'serene',
            'relaxed',
            'calm',
            'bored',
            'sluggish',
            'depressed',
            'sad'
            )
        workbook = queryset_to_workbook(queryset, columns)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export'+str(n)+'.xls"'
        workbook.save(response)
        n += 1

        return response


        """
        pomsmodel = cuestionarioPOMS.objects.all()
        # Attempt to grab information from the raw form information.

        #ejecutar solo una vez para llenar la tabla analysis, si se ejecurara nuevamente el experimento colocar en views de poms

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
    return render(request, 'analysis/index.html')

"""
    return render(request, 'analysis/index.html', {'coleram':coleram, 'coleras':coleras, 'fatigam':fatigam, 'fatigas':fatigas, \
                                               'vigorm':vigorm, 'vigors':vigors, 'amistadm':amistadm, 'amistads':amistads, \
                                               'tensionm':tensionm, 'tensions':tensions,'depresionm':depresionm, 'depresions':depresions})
"""
