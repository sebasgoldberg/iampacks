# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 16:07
from __future__ import unicode_literals

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('agencia', '0006_auto_20160319_1740'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='agencia',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='agencia',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='agenciado',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='sites.Site'),
        ),
    ]
