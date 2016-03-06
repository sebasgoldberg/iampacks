# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 20:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinvalido',
            name='fecha_deteccion',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 20, 44, 45, 759345), verbose_name='Fecha de detección'),
        ),
        migrations.AlterField(
            model_name='notificacioncuentaagenciadoexistente',
            name='fecha_envio',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 20, 44, 45, 758468), verbose_name='Fecha de envío'),
        ),
    ]
