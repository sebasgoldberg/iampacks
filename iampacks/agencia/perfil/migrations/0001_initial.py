# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Danza'
        db.create_table(u'perfil_danza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Danza'])

        # Adding model 'Deporte'
        db.create_table(u'perfil_deporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Deporte'])

        # Adding model 'EstadoDientes'
        db.create_table(u'perfil_estadodientes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['EstadoDientes'])

        # Adding model 'Idioma'
        db.create_table(u'perfil_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Idioma'])

        # Adding model 'Instrumento'
        db.create_table(u'perfil_instrumento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Instrumento'])

        # Adding model 'Ojos'
        db.create_table(u'perfil_ojos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Ojos'])

        # Adding model 'Pelo'
        db.create_table(u'perfil_pelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Pelo'])

        # Adding model 'Piel'
        db.create_table(u'perfil_piel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Piel'])

        # Adding model 'Talle'
        db.create_table(u'perfil_talle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'perfil', ['Talle'])


    def backwards(self, orm):
        # Deleting model 'Danza'
        db.delete_table(u'perfil_danza')

        # Deleting model 'Deporte'
        db.delete_table(u'perfil_deporte')

        # Deleting model 'EstadoDientes'
        db.delete_table(u'perfil_estadodientes')

        # Deleting model 'Idioma'
        db.delete_table(u'perfil_idioma')

        # Deleting model 'Instrumento'
        db.delete_table(u'perfil_instrumento')

        # Deleting model 'Ojos'
        db.delete_table(u'perfil_ojos')

        # Deleting model 'Pelo'
        db.delete_table(u'perfil_pelo')

        # Deleting model 'Piel'
        db.delete_table(u'perfil_piel')

        # Deleting model 'Talle'
        db.delete_table(u'perfil_talle')


    models = {
        u'perfil.danza': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Danza'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.deporte': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Deporte'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.estadodientes': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'EstadoDientes'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.idioma': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Idioma'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.instrumento': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Instrumento'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.ojos': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Ojos'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.pelo': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Pelo'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.piel': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Piel'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.talle': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Talle'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['perfil']