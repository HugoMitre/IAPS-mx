from django.shortcuts import render, get_object_or_404
from encuestas.forms import EncuestaForm, EncuestaDiscretaForm
from encuestas.models import ImagenIAPS, ImagenEncuesta
from encuestas.trigonometria import calculaAngulo
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def index(request, pk):
    # model =ImagenIAPS.objects.get(1)
    model = get_object_or_404(ImagenIAPS, pk=pk)
    imgIAPS=model.name
    neutra=model.neutral


    # If it's a HTTP POST, we're interested in processing form data.

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        form = EncuestaForm(data=request.POST)

        if form.is_valid():

            encuesta = form.save(commit=False)
            encuesta.persona_id = request.session['persona_id']
            encuesta.imagenIAPS = model

            encuesta.save()
            encuesta_id=encuesta.id

            return HttpResponseRedirect(reverse('encuestas:encuesta_discreta', kwargs={'pk': pk, 'encuesta_id':encuesta_id}))

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        #print request.session['persona_id']
        form = EncuestaForm()

    return render(request, 'encuestas/dimensional/index.html', {'form': form,'imgIAPS':imgIAPS,'neutra':neutra, 'pk':pk})

def encuesta_discreta(request, pk, encuesta_id):
    # model =ImagenIAPS.objects.get(1)
    model = get_object_or_404(ImagenEncuesta, pk=encuesta_id)

    x= model.valencia-5
    y=model.activacion-5

    ang = calculaAngulo(x,y)

    # If it's a HTTP POST, we're interested in processing form data.


    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        form = EncuestaDiscretaForm(ang, data=request.POST, instance=model)

        if form.is_valid():

            encuesta = form.save(commit=False)
            encuesta.finished=1

            encuesta.save()

            pk = int(pk) +1

            if pk <=40:
                return HttpResponseRedirect(reverse('encuestas:index',kwargs={'pk': pk}))
            else:
                return HttpResponseRedirect(reverse('personas.views.fin'))


    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        #print request.session['persona_id']
        form = EncuestaDiscretaForm(ang, None, instance=model)

    return render(request, 'encuestas/discreta/index.html', {'form': form,'ang':ang})

def instrucciones(request):

    return render(request, 'encuestas/instrucciones.html')
