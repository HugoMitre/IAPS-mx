# -*- encoding: utf-8 -*-
from django import forms
from encuestas.models import ImagenEncuesta
from django.forms.widgets import RadioFieldRenderer
from django.utils.html import format_html_join
from django.utils.encoding import force_text

class RadioFieldWithoutULRenderer(RadioFieldRenderer):

    def render(self):
        return format_html_join(
            '\n',
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0}',
            [(force_text(w),) for w in self],
        )

class RadioFieldDiscrete(RadioFieldRenderer):

    def render(self):
        return format_html_join(
            '\n',
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0}',
            [(force_text(w), ) for w in self],
        )


class EncuestaForm(forms.ModelForm):

    CHOICES=[(9,'*'),(8,'*'),(7,'*'),(6,'*'),(5,'*'),(4,'*'),(3,'*'),(2,'*'),(1,'*')]


    valencia = forms.ChoiceField(label="Agrado-Desagrado", help_text="¿Qué tanto de agrado o desagrado la imagen anterior según las caras de estas imagenes?", choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldWithoutULRenderer))
    activacion = forms.ChoiceField(label="Activado-Dormido",help_text="¿Qué tanto te activa o desactiva la imagen anterior según las caras de estas imagenes?", choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldWithoutULRenderer))


    class Meta:
        model = ImagenEncuesta
        fields = ('valencia','activacion')


class EncuestaDiscretaForm(forms.ModelForm):
    CHOICES=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]

    upset = forms.IntegerField(label="Disgustado", widget=forms.HiddenInput(), required=False)

    stressed = forms.IntegerField(label="Estresado", widget=forms.HiddenInput(),required=False)
    nervous = forms.IntegerField(label="Nervioso", widget=forms.HiddenInput(),required=False)
    tense = forms.IntegerField(label="Tenso", widget=forms.HiddenInput(),required=False)
    alert = forms.IntegerField(label="Atento", widget=forms.HiddenInput(),required=False)

    excited = forms.IntegerField(label="Emocionado", widget=forms.HiddenInput(),required=False)
    enthusiastic = forms.IntegerField(label="Entusiasta", widget=forms.HiddenInput(),required=False)
    happy = forms.IntegerField(label="Feliz", widget=forms.HiddenInput(),required=False)

    contented = forms.IntegerField(label="Complacido", widget=forms.HiddenInput(),required=False)
    serene = forms.IntegerField(label="Sereno", widget=forms.HiddenInput(),required=False)
    relaxed = forms.IntegerField(label="Relajado", widget=forms.HiddenInput(),required=False)
    calm = forms.IntegerField(label="Calmado", widget=forms.HiddenInput(),required=False)
    bored = forms.IntegerField(label="Aburrido", widget=forms.HiddenInput(),required=False)
    sluggish = forms.IntegerField(label="Perezoso", widget=forms.HiddenInput(),required=False)
    depressed = forms.IntegerField(label="Deprimido",widget=forms.HiddenInput(),required=False)
    sad = forms.IntegerField(label="Triste",widget=forms.HiddenInput(),required=False)


    def __init__(self, ang, *args, **kwargs):
        super(EncuestaDiscretaForm, self).__init__(*args, **kwargs)
        CHOICES=[(1,1),(2,2),(3,3),(4,4),(5,5)]

        # self.fields['upset']= forms.ChoiceField(label="upset",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldWithoutULRenderer))

        if ang >= 0.0 and ang < 22.5:
            self.fields['enthusiastic']= forms.ChoiceField(label="Entusiasta",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['happy']= forms.ChoiceField(label="Feliz",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['contented']= forms.ChoiceField(label="Complacido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 22.5 and ang < 45.0:

            self.fields['excited']= forms.ChoiceField(label="Emocionado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['enthusiastic']= forms.ChoiceField(label="Entusiasta",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['happy']= forms.ChoiceField(label="Feliz",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))

        elif ang >= 45.0 and ang < 67.5:
            self.fields['alert']= forms.ChoiceField(label="Atento",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['excited']= forms.ChoiceField(label="Emocionado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['enthusiastic']= forms.ChoiceField(label="Entusiasta",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 67.5 and ang < 90.0:
            self.fields['tense']= forms.ChoiceField(label="Tenso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['alert']= forms.ChoiceField(label="Atento",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['excited']= forms.ChoiceField(label="Emocionado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 90.0 and ang < 112.5:
            self.fields['nervous']= forms.ChoiceField(label="Nervioso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['tense']= forms.ChoiceField(label="Tenso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['alert']= forms.ChoiceField(label="Atento",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 112.5 and ang < 135.0:
            self.fields['stressed']= forms.ChoiceField(label="Estresado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['nervous']= forms.ChoiceField(label="Nervioso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['tense']= forms.ChoiceField(label="Tenso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 135.0 and ang < 157.5:
            self.fields['upset']= forms.ChoiceField(label="Disgustado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['stressed']= forms.ChoiceField(label="Estresado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['nervous']= forms.ChoiceField(label="Nervioso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 157.5 and ang < 180.0:
            self.fields['sad']= forms.ChoiceField(label="Triste",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['upset']= forms.ChoiceField(label="Disgustado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['stressed']= forms.ChoiceField(label="Estresado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 180.0 and ang < 202.5:
            self.fields['depressed']= forms.ChoiceField(label="Deprimido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['sad']= forms.ChoiceField(label="Triste",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['upset']= forms.ChoiceField(label="Disgustado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 202.5 and ang < 225.0:
            self.fields['sluggish']= forms.ChoiceField(label="Perezoso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['depressed']= forms.ChoiceField(label="Deprimido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['sad']= forms.ChoiceField(label="Triste",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 225.0 and ang < 247.5:
            self.fields['bored']= forms.ChoiceField(label="Aburrido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['sluggish']= forms.ChoiceField(label="Perezoso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['depressed']= forms.ChoiceField(label="Deprimido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 247.5 and ang < 270.0:
            self.fields['calm']= forms.ChoiceField(label="Calmado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['bored']= forms.ChoiceField(label="Aburrido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['sluggish']= forms.ChoiceField(label="Perezoso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 270.0 and ang < 292.5:
            self.fields['relaxed']= forms.ChoiceField(label="Relajado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['calm']= forms.ChoiceField(label="Calmado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['bored']= forms.ChoiceField(label="Aburrido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 292.5 and ang < 315.0:
            self.fields['serene']= forms.ChoiceField(label="Sereno",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['relaxed']= forms.ChoiceField(label="Relajado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['calm']= forms.ChoiceField(label="Calmado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 315.0 and ang < 337.5:
            self.fields['contented']= forms.ChoiceField(label="Complacido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['serene']= forms.ChoiceField(label="Sereno",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['relaxed']= forms.ChoiceField(label="Relajado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
        elif ang >= 337.5 and ang < 360.0:
            self.fields['happy']= forms.ChoiceField(label="Feliz",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['contented']= forms.ChoiceField(label="Complacido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))
            self.fields['serene']= forms.ChoiceField(label="Sereno",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldDiscrete))


    class Meta:
        model = ImagenEncuesta


        fields = ('upset','stressed','nervous','tense','alert','excited','enthusiastic',\
              'happy','contented','serene','relaxed','calm','bored','sluggish','depressed','sad')
