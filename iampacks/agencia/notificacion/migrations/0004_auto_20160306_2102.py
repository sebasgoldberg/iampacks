# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 21:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notificacion', '0003_auto_20160306_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinvalido',
            name='fecha_deteccion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de detección'),
        ),
        migrations.AlterField(
            model_name='notificacioncuentaagenciadoexistente',
            name='fecha_envio',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 21, 2, 4, 203270), verbose_name='Fecha de envío'),
        ),
    ]
