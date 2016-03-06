# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Dança',
                'verbose_name_plural': 'Danças',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Esporte',
                'verbose_name_plural': 'Esportes',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='EstadoDientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Estado Dentes',
                'verbose_name_plural': 'Estados Dentes',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Ojos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Olhos',
                'verbose_name_plural': 'Olhos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Pelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Cabelo',
                'verbose_name_plural': 'Cabelos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Piel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Pele',
                'verbose_name_plural': 'Peles',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Talle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripção')),
            ],
            options={
                'verbose_name': 'Manequim',
                'verbose_name_plural': 'Manequims',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='TalleRopa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Talle Ropa',
                'verbose_name_plural': 'Talle Ropa',
                'ordering': ['descripcion'],
            },
        ),
    ]