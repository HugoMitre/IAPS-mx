from django.shortcuts import render
from poms.forms import PomsForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    # If it's a HTTP POST, we're interested in processing form data.


    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        form = PomsForm(data=request.POST)

        if form.is_valid():
            # Save the driver's form data to the database.
            poms = form.save(commit=False)
            poms.persona_id = request.session['persona_id']
            poms.save()

            return HttpResponseRedirect(reverse('encuestas:instrucciones'))

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        #print request.session['persona_id']
        form = PomsForm()

    return render(request, 'poms/index.html', {'form': form})