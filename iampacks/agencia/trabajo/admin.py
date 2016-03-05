# coding=utf-8
from iampacks.agencia.trabajo.models import Productora, Rol, ItemPortfolio, Trabajo, Postulacion, DireccionProductora, TelefonoProductora, EventoTrabajo, EventoRol
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django.forms.models import BaseInlineFormSet
from django.http import HttpResponseRedirect
from iampacks.agencia.agencia.admin import AgenciadoAdmin
from django.forms.widgets import Textarea
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.cross.direccion.admin import PaisDireccionModelListFilter, EstadoDireccionModelListFilter, CiudadDireccionModelListFilter, BaseDireccionInline
from iampacks.cross.direccion.forms import BaseDireccionForm

class PostulacionInline(admin.TabularInline):
  model=Postulacion
  extra=1
  readonly_fields=['thumbnail_agenciado_link', 'agenciado_admin_link', 'agenciado_telefonos']
  fields=['thumbnail_agenciado_link', 'agenciado_admin_link', 'agenciado', 'estado', 'agenciado_telefonos']
  raw_id_fields = ('agenciado',)
  autocomplete_lookup_fields = {
    'fk': ['agenciado'],
    }

class AgenciadoPostulacionInline(admin.TabularInline):
  model=Postulacion
  extra=1
  readonly_fields=['rol_admin_link']
  fields=['rol_admin_link', 'rol', 'estado']

class DireccionProductoraForm(BaseDireccionForm):
  class Meta:
    model=DireccionProductora

class DireccionProductoraInline(BaseDireccionInline):
  form=DireccionProductoraForm
  model=DireccionProductora
  extra = 1

class TelefonoProductoraInline(admin.TabularInline):
  model=TelefonoProductora
  extra = 1

class EventoInline(admin.StackedInline):
  extra=0
  fieldsets=[
    (None, 
      {'fields':[
        ('tipo', 'descripcion', 'fecha'),
        ('ciudad', ), 
        ('barrio', 'direccion',), 
        ('codigo_postal',)]}),
  ]
  raw_id_fields = ('ciudad',)
  autocomplete_lookup_fields = {
    'fk': ['ciudad'],
    }
  
class EventoTrabajoForm(BaseDireccionForm):
  class Meta:
    model=EventoTrabajo

class EventoTrabajoInline(EventoInline):
  form=EventoTrabajoForm
  model=EventoTrabajo

class EventodRolForm(BaseDireccionForm):
  class Meta:
    model=EventoRol

class EventoRolInline(EventoInline):
  form=EventodRolForm
  model=EventoRol

class TrabajoInline(admin.TabularInline):
  model = Trabajo
  extra = 1
  readonly_fields = [ 'admin_link' ]
  fields = ['admin_link', 'titulo', 'estado', 'fecha_ingreso', 'descripcion',]
  formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':4})},
  }

class PaisDireccionProductoraListFilter(PaisDireccionModelListFilter):
  direccion_model = DireccionProductora
  fk_field_model = 'productora'

class EstadoDireccionProductoraListFilter(EstadoDireccionModelListFilter):
  direccion_model = DireccionProductora
  fk_field_model = 'productora'

class CiudadDireccionProductoraListFilter(CiudadDireccionModelListFilter):
  direccion_model = DireccionProductora
  fk_field_model = 'productora'

class ProductoraAdmin(admin.ModelAdmin):
  inlines = [TelefonoProductoraInline, DireccionProductoraInline, TrabajoInline]
  list_display=[
    'id', 'nombre', 'mail', 'telefonos', 'trabajos_iniciados', 'trabajos_activos'
  ]
  list_display_links = ['id', 'nombre']
  search_fields=['nombre', 'id']
  list_filter = (PaisDireccionProductoraListFilter, EstadoDireccionProductoraListFilter, CiudadDireccionProductoraListFilter)

class RolAdmin(admin.ModelAdmin):
  readonly_fields=[
    'id', 'cantidad_postulados_casting', 'cantidad_seleccionados_casting',
    'cantidad_seleccionados_trabajo', 'cantidad_trabajos_realizados',
    'cantidad_trabajos_pagados', 'trabajo_admin_link',
  ]
  inlines=[EventoRolInline, PostulacionInline]
  fieldsets=[
    (None, {'fields':['id']}),
    (ugettext_lazy(u'Dados do rol procurado'), 
      {'fields':[('descripcion', 'trabajo', 'trabajo_admin_link' ), 'cache', ('caracteristicas',)]}),
    (ugettext_lazy(u'Dados das postulaçoes'), 
      { 'fields':[ 
        ('cantidad_postulados_casting', 'cantidad_seleccionados_casting', 
        'cantidad_seleccionados_trabajo',), 
        ('cantidad_trabajos_realizados', 'cantidad_trabajos_pagados'),
        ]}),
  ]
  list_display=[
    'id', 'descripcion', 'trabajo', 'cache', 'cantidad_postulados_casting', 
    'cantidad_seleccionados_casting', 'cantidad_seleccionados_trabajo', 
    'cantidad_trabajos_realizados', 'cantidad_trabajos_pagados', 'caracteristicas',
  ]
  list_display_links = ['id']
  list_filter=['trabajo__estado', 'trabajo']
  search_fields=['trabajo__titulo', 'descripcion', 'id']

class RolInline(admin.TabularInline):
  model=Rol
  extra=1
  readonly_fields=['admin_link']
  fields=['admin_link', 'descripcion', 'cache','caracteristicas']
  formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':4})},
  }

class TrabajoAdmin(admin.ModelAdmin):
  readonly_fields=['id','thumbnail_img_link', 'productora_admin_link']
  inlines=[EventoTrabajoInline,RolInline]
  list_display=['id','titulo', 'estado', 'publicado', 'descripcion', 
    'fecha_ingreso', 'roles']
  list_display_links = ('id', 'titulo')
  list_filter=['estado', 'publicado']
  search_fields=['titulo','id']
  date_hierarchy='fecha_ingreso'
  fieldsets=[
    (None, {'fields':['id', 'thumbnail_img_link']}),
    (ugettext_lazy(u'Dados do trabalho'), 
      {'fields':['titulo', ('productora', 'productora_admin_link'), 'estado', 'fecha_ingreso', 'publicado', 'descripcion', 'imagen']}),
  ]

class PostulacionAdmin(admin.ModelAdmin):
  readonly_fields=['id']
  list_display=['id', 'trabajo_rol', 'rol', 'thumbnail_agenciado_link', 'agenciado', 'estado']
  list_display_links = ('id',)
  list_filter=['rol', 'estado']
  search_fields=['trabajo__titulo', 'rol__descripcion', 'agenciado__nombre', 'agenciado__apellido', 'id']
  list_editable=['estado']

class ItemPortfolioAdmin(admin.ModelAdmin):
  readonly_fields=['id','html_media']
  list_display=['html_small_media', 'titulo', 'id', 'fecha']
  list_display_links = ('id', 'titulo')
  search_fields=['titulo']
  fieldsets=[
    (None, {'fields':['html_media','id']}),
    ('Dados do item do portifolio', 
      {'fields':['titulo', 'fecha', 'video', 'imagen']})
  ]
  list_per_page = 10

def add_agenciados_trabajo(modeladmin, request, queryset):
  selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
  return HttpResponseRedirect("/trabajo/agregar/agenciados/seleccionados/a/rol/?ids=%s" %  ",".join(selected))

add_agenciados_trabajo.short_description=ugettext_lazy(u'Adicionar agenciados selecionados a perfil procurado em trabalho')

# IMPORTANTE: El agregado de la accion se hace de la siguiente forma porque si solo se hiciese con '+=' y el listado estuviese vacío, entonces la acción se registraría para todos los modelos. Este imagino que debe ser un bug de django. Con append ocurre el mismo error.
if len(AgenciadoAdmin.actions)==0:
  AgenciadoAdmin.actions=[add_agenciados_trabajo]
else:
  AgenciadoAdmin.actions+=[add_agenciados_trabajo]

AgenciadoAdmin.inlines+=[AgenciadoPostulacionInline]

admin.site.register(Productora,ProductoraAdmin)
admin.site.register(Rol,RolAdmin)
admin.site.register(ItemPortfolio,ItemPortfolioAdmin)
admin.site.register(Trabajo,TrabajoAdmin)
#admin.site.register(Postulacion,PostulacionAdmin)
