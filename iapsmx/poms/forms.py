# -*- encoding: utf-8 -*-
from django import forms
from poms.models import cuestionarioPOMS
from django.forms.widgets import RadioFieldRenderer
from django.utils.html import format_html_join
from django.utils.encoding import force_text

class RadioFieldPOMS(RadioFieldRenderer):

    def render(self):
        return format_html_join(
            '',
            '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0}',
            [(force_text(w), ) for w in self],
        )


class PomsForm(forms.ModelForm):

    CHOICES=[(0,0),(1,1),(2,2),(3,3),(4,4)]

    enfadado = forms.ChoiceField(label="Enfadado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    agotado = forms.ChoiceField(label="Agotado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    llenoEnergia = forms.ChoiceField(label="Lleno de energia",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    amable = forms.ChoiceField(label="Amable",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    conNerviosPunta = forms.ChoiceField(label="Nervios de Punta",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    infeliz=forms.ChoiceField(label="Infeliz",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))

    malhumorado=forms.ChoiceField(label="Malhumorado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    fatigado=forms.ChoiceField(label="Fatigado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    energico=forms.ChoiceField(label="Energico",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    comprensivo=forms.ChoiceField(label="Comprensivo",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    nervioso=forms.ChoiceField(label="Nervioso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    triste=forms.ChoiceField(label="Triste",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))

    irritable=forms.ChoiceField(label="Irritable",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    cansado=forms.ChoiceField(label="Cansado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    activo=forms.ChoiceField(label="Activo",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    servicial=forms.ChoiceField(label="Servicial",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    tenso=forms.ChoiceField(label="Tenso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    desesperanzado=forms.ChoiceField(label="Desesperanzado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))

    molesto=forms.ChoiceField(label="Molesto",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    debil=forms.ChoiceField(label="Debil",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    animado=forms.ChoiceField(label="Animado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    amistoso=forms.ChoiceField(label="Amistoso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    agitado=forms.ChoiceField(label="Agitado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    solo=forms.ChoiceField(label="Solo",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))

    resentido=forms.ChoiceField(label="Resentido",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    exhausto=forms.ChoiceField(label="Exhausto",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    vigoroso=forms.ChoiceField(label="Vigoroso",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    consideradoConDemas=forms.ChoiceField(label="Considerado",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    inquieto=forms.ChoiceField(label="Inquieto",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))
    melancolico=forms.ChoiceField(label="Melancolico",choices=CHOICES, widget=forms.RadioSelect(renderer=RadioFieldPOMS))



    class Meta:
        model = cuestionarioPOMS
        exclude = ('persona',)