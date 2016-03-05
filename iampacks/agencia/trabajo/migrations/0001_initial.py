# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Productora'
        db.create_table(u'trabajo_productora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'trabajo', ['Productora'])

        # Adding model 'DireccionProductora'
        db.create_table(u'trabajo_direccionproductora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('productora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Productora'])),
        ))
        db.send_create_signal(u'trabajo', ['DireccionProductora'])

        # Adding model 'TelefonoProductora'
        db.create_table(u'trabajo_telefonoproductora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['telefono.Compania'], null=True, on_delete=models.PROTECT, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('productora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Productora'])),
        ))
        db.send_create_signal(u'trabajo', ['TelefonoProductora'])

        # Adding model 'ItemPortfolio'
        db.create_table(u'trabajo_itemportfolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True, null=True, blank=True)),
            ('codigo_video', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True, null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 16, 0, 0))),
        ))
        db.send_create_signal(u'trabajo', ['ItemPortfolio'])

        # Adding model 'Trabajo'
        db.create_table(u'trabajo_trabajo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('productora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Productora'], on_delete=models.PROTECT)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 16, 0, 0))),
            ('publicado', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'trabajo', ['Trabajo'])

        # Adding model 'EventoTrabajo'
        db.create_table(u'trabajo_eventotrabajo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 16, 0, 0), null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('trabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Trabajo'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'trabajo', ['EventoTrabajo'])

        # Adding model 'Rol'
        db.create_table(u'trabajo_rol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Trabajo'], on_delete=models.PROTECT)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('cache', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=4, blank=True)),
            ('caracteristicas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'trabajo', ['Rol'])

        # Adding unique constraint on 'Rol', fields ['trabajo', 'descripcion']
        db.create_unique(u'trabajo_rol', ['trabajo_id', 'descripcion'])

        # Adding model 'EventoRol'
        db.create_table(u'trabajo_eventorol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 16, 0, 0), null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Rol'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'trabajo', ['EventoRol'])

        # Adding model 'Postulacion'
        db.create_table(u'trabajo_postulacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agenciado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agenciado'], on_delete=models.PROTECT)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabajo.Rol'], on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'trabajo', ['Postulacion'])

        # Adding unique constraint on 'Postulacion', fields ['agenciado', 'rol']
        db.create_unique(u'trabajo_postulacion', ['agenciado_id', 'rol_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Postulacion', fields ['agenciado', 'rol']
        db.delete_unique(u'trabajo_postulacion', ['agenciado_id', 'rol_id'])

        # Removing unique constraint on 'Rol', fields ['trabajo', 'descripcion']
        db.delete_unique(u'trabajo_rol', ['trabajo_id', 'descripcion'])

        # Deleting model 'Productora'
        db.delete_table(u'trabajo_productora')

        # Deleting model 'DireccionProductora'
        db.delete_table(u'trabajo_direccionproductora')

        # Deleting model 'TelefonoProductora'
        db.delete_table(u'trabajo_telefonoproductora')

        # Deleting model 'ItemPortfolio'
        db.delete_table(u'trabajo_itemportfolio')

        # Deleting model 'Trabajo'
        db.delete_table(u'trabajo_trabajo')

        # Deleting model 'EventoTrabajo'
        db.delete_table(u'trabajo_eventotrabajo')

        # Deleting model 'Rol'
        db.delete_table(u'trabajo_rol')

        # Deleting model 'EventoRol'
        db.delete_table(u'trabajo_eventorol')

        # Deleting model 'Postulacion'
        db.delete_table(u'trabajo_postulacion')


    models = {
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
            'documento_rg': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'estado_dientes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.EstadoDientes']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 16, 0, 0)'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idiomas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Idioma']", 'symmetrical': 'False', 'blank': 'True'}),
            'indicador_maneja': ('django.db.models.fields.BooleanField', [], {}),
            'indicador_tiene_registro': ('django.db.models.fields.BooleanField', [], {}),
            'instrumentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfil.Instrumento']", 'symmetrical': 'False', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ojos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Ojos']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'pelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Pelo']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'piel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Piel']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'talle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfil.Talle']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'talle_camisa': ('django.db.models.fields.IntegerField', [], {}),
            'talle_pantalon': ('django.db.models.fields.IntegerField', [], {}),
            'trabaja_como_extra': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
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
        },
        u'telefono.compania': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Compania'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'trabajo.direccionproductora': {
            'Meta': {'object_name': 'DireccionProductora'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'productora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Productora']"})
        },
        u'trabajo.eventorol': {
            'Meta': {'object_name': 'EventoRol'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 16, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Rol']", 'on_delete': 'models.PROTECT'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'trabajo.eventotrabajo': {
            'Meta': {'object_name': 'EventoTrabajo'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 16, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'trabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Trabajo']", 'on_delete': 'models.PROTECT'})
        },
        u'trabajo.itemportfolio': {
            'Meta': {'ordering': "['-fecha']", 'object_name': 'ItemPortfolio'},
            'codigo_video': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'trabajo.postulacion': {
            'Meta': {'ordering': "['-rol__trabajo__fecha_ingreso', 'rol__descripcion', 'agenciado__nombre', 'agenciado__apellido']", 'unique_together': "(('agenciado', 'rol'),)", 'object_name': 'Postulacion'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']", 'on_delete': 'models.PROTECT'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Rol']", 'on_delete': 'models.PROTECT'})
        },
        u'trabajo.productora': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Productora'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'trabajo.rol': {
            'Meta': {'ordering': "['-trabajo__fecha_ingreso', 'descripcion']", 'unique_together': "(('trabajo', 'descripcion'),)", 'object_name': 'Rol'},
            'cache': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '4', 'blank': 'True'}),
            'caracteristicas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Trabajo']", 'on_delete': 'models.PROTECT'})
        },
        u'trabajo.telefonoproductora': {
            'Meta': {'object_name': 'TelefonoProductora'},
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['telefono.Compania']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Productora']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'trabajo.trabajo': {
            'Meta': {'ordering': "['-fecha_ingreso']", 'object_name': 'Trabajo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'productora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trabajo.Productora']", 'on_delete': 'models.PROTECT'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['trabajo']