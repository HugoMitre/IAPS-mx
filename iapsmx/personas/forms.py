# -*- encoding: utf-8 -*-
from django import forms
from personas.models import Persona


class PersonaForm(forms.ModelForm):


    edad = forms.IntegerField(min_value=18, label="Edad",
                                              widget=forms.NumberInput(attrs={'class': 'numeric form-control'}),
                                              error_messages={'min_value': 'Incorrect value.'})


    dynamic_choices_estado = (
        (None, '--------------'),
        (1, 'Aguascalientes'),
        (2, 'Baja California'),
        (3, 'Baja California Sur'),
        (4, 'Campeche'),
        (5, 'Chiapas'),
        (6, 'Chihuahua'),
        (7, 'Coahuila'),
        (8, 'Colima'),
        (9, 'Distrito Federal'),
        (10, 'Durango'),
        (11, 'Estado de México'),
        (12, 'Guanajuato'),
        (13, 'Guerrero'),
        (14, 'Hidalgo'),
        (15, 'Jalisco'),
        (16, 'Michoacán'),
        (17, 'Morelos'),
        (18, 'Nayarit'),
        (19, 'Nuevo León'),
        (20, 'Oaxaca'),
        (21, 'Puebla'),
        (22, 'Querétaro'),
        (23, 'Quintana Roo'),
        (24, 'San Luis Potosí'),
        (25, 'Sinaloa'),
        (26, 'Sonora'),
        (27, 'Tabasco'),
        (28, 'Tamaulipas'),
        (29, 'Tlaxcala'),
        (30, 'Veracruz'),
        (31, 'Yucatán'),
        (32, 'Zacatecas'),

    )
    estado = forms.ChoiceField(label="Estado donde te criaste", required=True,
                                 choices=dynamic_choices_estado, help_text="Selecciona el estado donde has vivido más tiempo",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    dynamic_choices_gender = (
        (None, '--------------'),
        (0, 'Masculino'),
        (2, 'Femenino'),
    )

    genero = forms.ChoiceField(label="Genero", required=True,
                                 choices=dynamic_choices_gender, help_text="Selecciona tu genero",
                                 widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Persona
        fields = ('edad','estado','genero')