# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0005_auto_20160306_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='foto_agenciado_obligatoria',
            field=models.BooleanField(default=None, verbose_name='Foto Agenciado Obligatoria'),
        ),
    ]
