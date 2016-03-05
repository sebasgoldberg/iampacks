# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compania'
        db.create_table(u'telefono_compania', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'telefono', ['Compania'])


    def backwards(self, orm):
        # Deleting model 'Compania'
        db.delete_table(u'telefono_compania')


    models = {
        u'telefono.compania': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Compania'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['telefono']