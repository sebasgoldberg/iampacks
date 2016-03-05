# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'TrabajoRealizadoAgenciado', fields ['descripcion']
        db.delete_unique(u'agencia_trabajorealizadoagenciado', ['descripcion'])

        # Removing unique constraint on 'TrabajoVigenteAgenciado', fields ['descripcion']
        db.delete_unique(u'agencia_trabajovigenteagenciado', ['descripcion'])


    def backwards(self, orm):
        # Adding unique constraint on 'TrabajoVigenteAgenciado', fields ['descripcion']
        db.create_unique(u'agencia_trabajovigenteagenciado', ['descripcion'])

        # Adding unique constraint on 'TrabajoRealizadoAgenciado', fields ['descripcion']
        db.create_unique(u'agencia_trabajorealizadoagenciado', ['descripcion'])


    models = {
        u'agencia.agencia': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Agencia'},
            'activa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'favicon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mapa_contacto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'presentacion_home': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo_home': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'agencia.agenciado': {
            'Meta': {'ordering': "['nombre', 'apellido']", 'object_name': 'Agenciado'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'altura': ('django.db.models.fields.FloatField', [], {}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'calzado': ('django.db.models.fields.IntegerField', [], {}),
            'como_nos_conocio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cuenta_bancaria': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'danzas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Danza']", 'symmetrical': 'False', 'blank': 'True'}),
            'deportes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Deporte']", 'symmetrical': 'False', 'blank': 'True'}),
            'documento_cpf': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'documento_drt': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'documento_rg': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'estado_dientes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.EstadoDientes']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idiomas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Idioma']", 'symmetrical': 'False', 'blank': 'True'}),
            'indicador_maneja': ('django.db.models.fields.BooleanField', [], {}),
            'indicador_tiene_registro': ('django.db.models.fields.BooleanField', [], {}),
            'instrumentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Instrumento']", 'symmetrical': 'False', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nombre_artistico': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '121'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ojos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Ojos']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'pelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Pelo']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'piel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Piel']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'referente': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['agencia.Agenciador']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'talle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Talle']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'talle_camisa': ('django.db.models.fields.IntegerField', [], {}),
            'talle_pantalon': ('django.db.models.fields.IntegerField', [], {}),
            'talle_ropa_camisa': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'camisa'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['perfil.TalleRopa']"}),
            'talle_ropa_pantalon': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pantalon'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['perfil.TalleRopa']"}),
            'trabaja_como_extra': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'agencia.agenciador': {
            'Meta': {'object_name': 'Agenciador'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'agencia.direccionagencia': {
            'Meta': {'object_name': 'DireccionAgencia'},
            'agencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agencia']"}),
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'})
        },
        u'agencia.direccionagenciado': {
            'Meta': {'object_name': 'DireccionAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'})
        },
        u'agencia.disponibilidadtrabajoagenciado': {
            'Meta': {'object_name': 'DisponibilidadTrabajoAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'dia_desde': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'dia_hasta': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hora_desde': ('django.db.models.fields.TimeField', [], {}),
            'hora_hasta': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencia.fotoagenciado': {
            'Meta': {'object_name': 'FotoAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencia.mailagenciado': {
            'Meta': {'object_name': 'MailAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencia.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['telefono.Compania']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'agencia.telefonoagencia': {
            'Meta': {'object_name': 'TelefonoAgencia'},
            'agencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agencia']"}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['telefono.Compania']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'agencia.trabajorealizadoagenciado': {
            'Meta': {'object_name': 'TrabajoRealizadoAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_desde': ('django.db.models.fields.DateField', [], {}),
            'fecha_hasta': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencia.trabajovigenteagenciado': {
            'Meta': {'object_name': 'TrabajoVigenteAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_vigencia': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'agencia.videoagenciado': {
            'Meta': {'object_name': 'VideoAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'codigo_video': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cities_light.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.region': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'perfil.talleropa': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'TalleRopa'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'telefono.compania': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Compania'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['agencia']