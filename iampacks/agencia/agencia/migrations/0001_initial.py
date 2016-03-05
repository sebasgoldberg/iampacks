# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agencia'
        db.create_table(u'agencia_agencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('activa', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('favicon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('titulo_home', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('presentacion_home', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mapa_contacto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'agencia', ['Agencia'])

        # Adding model 'TelefonoAgencia'
        db.create_table(u'agencia_telefonoagencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['telefono.Compania'], null=True, on_delete=models.PROTECT, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('agencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agencia'])),
        ))
        db.send_create_signal(u'agencia', ['TelefonoAgencia'])

        # Adding model 'DireccionAgencia'
        db.create_table(u'agencia_direccionagencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('agencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agencia'])),
        ))
        db.send_create_signal(u'agencia', ['DireccionAgencia'])

        # Adding model 'Agenciado'
        db.create_table(u'agencia_agenciado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('documento_rg', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('documento_cpf', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('responsable', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('cuenta_bancaria', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ojos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfil.Ojos'], null=True, on_delete=models.PROTECT)),
            ('pelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfil.Pelo'], null=True, on_delete=models.PROTECT)),
            ('piel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfil.Piel'], null=True, on_delete=models.PROTECT)),
            ('altura', self.gf('django.db.models.fields.FloatField')()),
            ('peso', self.gf('django.db.models.fields.FloatField')()),
            ('talle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfil.Talle'], null=True, on_delete=models.PROTECT)),
            ('talle_camisa', self.gf('django.db.models.fields.IntegerField')()),
            ('talle_pantalon', self.gf('django.db.models.fields.IntegerField')()),
            ('calzado', self.gf('django.db.models.fields.IntegerField')()),
            ('estado_dientes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfil.EstadoDientes'], null=True, on_delete=models.PROTECT)),
            ('indicador_maneja', self.gf('django.db.models.fields.BooleanField')()),
            ('indicador_tiene_registro', self.gf('django.db.models.fields.BooleanField')()),
            ('trabaja_como_extra', self.gf('django.db.models.fields.BooleanField')()),
            ('como_nos_conocio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 16, 0, 0))),
            ('recurso_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'agencia', ['Agenciado'])

        # Adding M2M table for field deportes on 'Agenciado'
        m2m_table_name = db.shorten_name(u'agencia_agenciado_deportes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agenciado', models.ForeignKey(orm[u'agencia.agenciado'], null=False)),
            ('deporte', models.ForeignKey(orm[u'perfil.deporte'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agenciado_id', 'deporte_id'])

        # Adding M2M table for field danzas on 'Agenciado'
        m2m_table_name = db.shorten_name(u'agencia_agenciado_danzas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agenciado', models.ForeignKey(orm[u'agencia.agenciado'], null=False)),
            ('danza', models.ForeignKey(orm[u'perfil.danza'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agenciado_id', 'danza_id'])

        # Adding M2M table for field instrumentos on 'Agenciado'
        m2m_table_name = db.shorten_name(u'agencia_agenciado_instrumentos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agenciado', models.ForeignKey(orm[u'agencia.agenciado'], null=False)),
            ('instrumento', models.ForeignKey(orm[u'perfil.instrumento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agenciado_id', 'instrumento_id'])

        # Adding M2M table for field idiomas on 'Agenciado'
        m2m_table_name = db.shorten_name(u'agencia_agenciado_idiomas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agenciado', models.ForeignKey(orm[u'agencia.agenciado'], null=False)),
            ('idioma', models.ForeignKey(orm[u'perfil.idioma'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agenciado_id', 'idioma_id'])

        # Adding model 'DireccionAgenciado'
        db.create_table(u'agencia_direccionagenciado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('agenciado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agenciado'])),
        ))
        db.send_create_signal(u'agencia', ['DireccionAgenciado'])

        # Adding model 'FotoAgenciado'
        db.create_table(u'agencia_fotoagenciado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agenciado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agenciado'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'agencia', ['FotoAgenciado'])

        # Adding model 'VideoAgenciado'
        db.create_table(u'agencia_videoagenciado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True, null=True, blank=True)),
            ('codigo_video', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True, null=True, blank=True)),
            ('agenciado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agenciado'])),
        ))
        db.send_create_signal(u'agencia', ['VideoAgenciado'])

        # Adding model 'Telefono'
        db.create_table(u'agencia_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['telefono.Compania'], null=True, on_delete=models.PROTECT, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('agenciado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencia.Agenciado'])),
        ))
        db.send_create_signal(u'agencia', ['Telefono'])


    def backwards(self, orm):
        # Deleting model 'Agencia'
        db.delete_table(u'agencia_agencia')

        # Deleting model 'TelefonoAgencia'
        db.delete_table(u'agencia_telefonoagencia')

        # Deleting model 'DireccionAgencia'
        db.delete_table(u'agencia_direccionagencia')

        # Deleting model 'Agenciado'
        db.delete_table(u'agencia_agenciado')

        # Removing M2M table for field deportes on 'Agenciado'
        db.delete_table(db.shorten_name(u'agencia_agenciado_deportes'))

        # Removing M2M table for field danzas on 'Agenciado'
        db.delete_table(db.shorten_name(u'agencia_agenciado_danzas'))

        # Removing M2M table for field instrumentos on 'Agenciado'
        db.delete_table(db.shorten_name(u'agencia_agenciado_instrumentos'))

        # Removing M2M table for field idiomas on 'Agenciado'
        db.delete_table(db.shorten_name(u'agencia_agenciado_idiomas'))

        # Deleting model 'DireccionAgenciado'
        db.delete_table(u'agencia_direccionagenciado')

        # Deleting model 'FotoAgenciado'
        db.delete_table(u'agencia_fotoagenciado')

        # Deleting model 'VideoAgenciado'
        db.delete_table(u'agencia_videoagenciado')

        # Deleting model 'Telefono'
        db.delete_table(u'agencia_telefono')


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
        u'agencia.fotoagenciado': {
            'Meta': {'object_name': 'FotoAgenciado'},
            'agenciado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencia.Agenciado']"}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['agencia']