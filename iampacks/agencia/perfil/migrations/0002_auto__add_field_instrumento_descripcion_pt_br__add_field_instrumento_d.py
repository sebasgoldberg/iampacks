# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Instrumento.descripcion_pt_br'
        db.add_column(u'perfil_instrumento', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Instrumento.descripcion_es'
        db.add_column(u'perfil_instrumento', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Pelo.descripcion_pt_br'
        db.add_column(u'perfil_pelo', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Pelo.descripcion_es'
        db.add_column(u'perfil_pelo', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Danza.descripcion_pt_br'
        db.add_column(u'perfil_danza', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Danza.descripcion_es'
        db.add_column(u'perfil_danza', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Deporte.descripcion_pt_br'
        db.add_column(u'perfil_deporte', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Deporte.descripcion_es'
        db.add_column(u'perfil_deporte', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ojos.descripcion_pt_br'
        db.add_column(u'perfil_ojos', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ojos.descripcion_es'
        db.add_column(u'perfil_ojos', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EstadoDientes.descripcion_pt_br'
        db.add_column(u'perfil_estadodientes', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EstadoDientes.descripcion_es'
        db.add_column(u'perfil_estadodientes', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Piel.descripcion_pt_br'
        db.add_column(u'perfil_piel', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Piel.descripcion_es'
        db.add_column(u'perfil_piel', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Talle.descripcion_pt_br'
        db.add_column(u'perfil_talle', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Talle.descripcion_es'
        db.add_column(u'perfil_talle', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Idioma.descripcion_pt_br'
        db.add_column(u'perfil_idioma', 'descripcion_pt_br',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Idioma.descripcion_es'
        db.add_column(u'perfil_idioma', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Instrumento.descripcion_pt_br'
        db.delete_column(u'perfil_instrumento', 'descripcion_pt_br')

        # Deleting field 'Instrumento.descripcion_es'
        db.delete_column(u'perfil_instrumento', 'descripcion_es')

        # Deleting field 'Pelo.descripcion_pt_br'
        db.delete_column(u'perfil_pelo', 'descripcion_pt_br')

        # Deleting field 'Pelo.descripcion_es'
        db.delete_column(u'perfil_pelo', 'descripcion_es')

        # Deleting field 'Danza.descripcion_pt_br'
        db.delete_column(u'perfil_danza', 'descripcion_pt_br')

        # Deleting field 'Danza.descripcion_es'
        db.delete_column(u'perfil_danza', 'descripcion_es')

        # Deleting field 'Deporte.descripcion_pt_br'
        db.delete_column(u'perfil_deporte', 'descripcion_pt_br')

        # Deleting field 'Deporte.descripcion_es'
        db.delete_column(u'perfil_deporte', 'descripcion_es')

        # Deleting field 'Ojos.descripcion_pt_br'
        db.delete_column(u'perfil_ojos', 'descripcion_pt_br')

        # Deleting field 'Ojos.descripcion_es'
        db.delete_column(u'perfil_ojos', 'descripcion_es')

        # Deleting field 'EstadoDientes.descripcion_pt_br'
        db.delete_column(u'perfil_estadodientes', 'descripcion_pt_br')

        # Deleting field 'EstadoDientes.descripcion_es'
        db.delete_column(u'perfil_estadodientes', 'descripcion_es')

        # Deleting field 'Piel.descripcion_pt_br'
        db.delete_column(u'perfil_piel', 'descripcion_pt_br')

        # Deleting field 'Piel.descripcion_es'
        db.delete_column(u'perfil_piel', 'descripcion_es')

        # Deleting field 'Talle.descripcion_pt_br'
        db.delete_column(u'perfil_talle', 'descripcion_pt_br')

        # Deleting field 'Talle.descripcion_es'
        db.delete_column(u'perfil_talle', 'descripcion_es')

        # Deleting field 'Idioma.descripcion_pt_br'
        db.delete_column(u'perfil_idioma', 'descripcion_pt_br')

        # Deleting field 'Idioma.descripcion_es'
        db.delete_column(u'perfil_idioma', 'descripcion_es')


    models = {
        u'perfil.danza': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Danza'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.deporte': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Deporte'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.estadodientes': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'EstadoDientes'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.idioma': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Idioma'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.instrumento': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Instrumento'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.ojos': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Ojos'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.pelo': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Pelo'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.piel': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Piel'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'perfil.talle': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Talle'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['perfil']