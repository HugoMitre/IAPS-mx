# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '__first__'),
        ('poms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='factorPOMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colera', models.IntegerField()),
                ('fatiga', models.IntegerField()),
                ('vigor', models.IntegerField()),
                ('amistad', models.IntegerField()),
                ('tension', models.IntegerField()),
                ('deprimido', models.IntegerField()),
                ('persona', models.OneToOneField(to='personas.Persona')),
                ('poms', models.OneToOneField(to='poms.cuestionarioPOMS')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
