from django.http import HttpResponseRedirect
from django.shortcuts import render
from personas.forms import PersonaForm
from django.core.urlresolvers import reverse



def index(request):

    # If it's a HTTP POST, we're interested in processing form data.

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        form = PersonaForm(data=request.POST)

        if form.is_valid():
            # Save the driver's form data to the database.
            persona = form.save(commit=False)

            persona.save()

            request.session['persona_id']= persona.id

            return HttpResponseRedirect(reverse('poms:index'))

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        form = PersonaForm()

    return render(request, 'personas/index.html', {'form': form})

def home(request):

    return render(request, 'index.html')

def fin(request):

    return render(request, 'fin.html')