# coding=utf-8

from django.db import models
from iampacks.agencia.agencia.models import Agenciado
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from datetime import date, datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.cross.direccion.models import Direccion
from iampacks.cross.telefono.models import Telefono

class Evento(Direccion):
  fecha = models.DateTimeField(default=datetime.today(),verbose_name=ugettext_lazy(u'Data do evento'), blank=True, null=True)
  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u'Evento')
    verbose_name_plural = ugettext_lazy(u'Eventos')

class Productora(models.Model):
  user= models.OneToOneField(User, null=True, blank=True, editable=False)

  # Datos 
  nombre = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Nome'))
  mail = models.EmailField(verbose_name=ugettext_lazy(u'e-mail'))

  imagen = models.ImageField(upload_to='trabajo/productora/', null=True, blank=True)
  thumbnail = ImageSpecField(
    [Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)],
    source='imagen', format='JPEG', options={'quality': 90}
    )
  def __unicode__(self):
    return self.nombre
  class Meta:
    ordering = ['nombre']
    verbose_name = ugettext_lazy(u"Produtora")
    verbose_name_plural = ugettext_lazy(u"Produtoras")

  def telefonos(self):
    html = '<ul>'
    for telefono in self.telefonoproductora_set.all():
      html += '<li>%s</li>'%telefono
    html += '</ul>'
    return html
  telefonos.allow_tags = True
  telefonos.short_description = ugettext_lazy(u'Telefones')

  def trabajos_activos(self):
    html = '<ul>'
    for trabajo in Trabajo.filter_activos(self.trabajo_set):
      html += '<li>%s</li>'%trabajo.admin_link()
    html += '</ul>'
    return html
  trabajos_activos.allow_tags = True
  trabajos_activos.short_description = ugettext_lazy(u'Trabalhos ativos')
    
  def trabajos_iniciados(self):
    html = '<ul>'
    for trabajo in Trabajo.filter_iniciados(self.trabajo_set):
      html += '<li>%s</li>'%trabajo.admin_link()
    html += '</ul>'
    return html
  trabajos_iniciados.allow_tags = True
  trabajos_iniciados.short_description = ugettext_lazy(u'Trabalhos iniciados')
    
class DireccionProductora(Direccion):
  productora = models.ForeignKey(Productora, verbose_name=ugettext_lazy(u'Produtora'))
  def __unicode__(self):
    return "%s, %s, %s, %s" % (self.direccion, self.barrio, self.ciudad, self.codigo_postal)

class TelefonoProductora(Telefono):
  productora = models.ForeignKey(Productora, verbose_name=ugettext_lazy(u'Produtora'))

class ItemPortfolio(models.Model):
    titulo = models.CharField(max_length=100, unique_for_date='fecha')
    video = models.URLField(unique=True, null=True, blank=True)
    codigo_video = models.CharField(max_length=30, unique=True, null=True, blank=True)
    # agregar rutas a configuracion del apache, al archivo settings y crear carpetas correspondientes
    imagen = models.ImageField(upload_to='trabajo/portfolio/', null=True, blank=True)
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(358,202)], source='imagen', format='JPEG', options={'quality': 90})
    fecha = models.DateField(default=date.today(),verbose_name=ugettext_lazy(u'Data'))
    def __unicode__(self):
      return self.titulo
    class Meta:
      ordering = ['-fecha']
      verbose_name = ugettext_lazy(u"Item Portfolio")
      verbose_name_plural = ugettext_lazy(u"Portfolio")
    def get_youtube_iframe_url(self):
      return (u'https://www.youtube.com/embed/%s' % self.codigo_video)
    get_youtube_iframe_url.allow_tags = True
    def html_youtube_iframe(self):
      return '<iframe width="358" height="202" src="%s" frameborder="0" allowfullscreen></iframe>' % self.get_youtube_iframe_url()
    html_youtube_iframe.allow_tags = True 
    html_youtube_iframe.short_description = ugettext_lazy('Video')
    def html_small_youtube_iframe(self):
      return u'<iframe width="186" height="105" src="%s" frameborder="0" allowfullscreen></iframe>' % self.get_youtube_iframe_url()
    html_small_youtube_iframe.allow_tags = True 
    html_small_youtube_iframe.short_description = ugettext_lazy(u'Video')
    def html_media(self):
      if self.codigo_video:
        return self.html_youtube_iframe()
      else:
        return self.html_thumbnail()
    html_media.allow_tags = True
    html_media.short_description = ugettext_lazy(u'Video ou imagem')
    def html_small_media(self):
      if self.codigo_video:
        return self.html_small_youtube_iframe()
      else:
        return self.html_thumbnail()
    html_small_media.allow_tags = True
    html_small_media.short_description = ugettext_lazy(u'Video ou imagem')
    def html_thumbnail(self):
      if not self.imagen:
        return
      return "<a href='%s'><img src='%s'/></a>" % (self.imagen.url, self.thumbnail.url)

    def url_to_codigo_video(self):
      if self.video is None:
        return
      if re.search('^.*v=',self.video):
        self.codigo_video = re.sub('^.*v=','',self.video)
        self.codigo_video = re.sub('&.*$','',self.codigo_video)
      elif re.search('[^?]',self.video):
        self.codigo_video = re.sub('^.*/','',self.video)

@receiver(pre_save, sender=ItemPortfolio)
def callback_save_item_portfolio(sender, instance, raw, using, **kwargs):
  instance.url_to_codigo_video()

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100, unique_for_date='fecha_ingreso')
    productora= models.ForeignKey(Productora,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Produtora'))
    descripcion = models.TextField(verbose_name=ugettext_lazy(u'Descripção'), null=True, blank=True)
    imagen = models.ImageField(upload_to='trabajo/trabajo/',blank=True)
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)], source='imagen', format='JPEG', options={'quality': 90})
    ESTADO_TRABAJO=(
      ('IN',_(u'Inicial')),
      ('AT',_(u'Ativo')),
      ('PC',_(u'Pendente de cobrar')),
      ('FI',_(u'Finalizado')),
    )
    estado = models.CharField(max_length=2,choices=ESTADO_TRABAJO,null=False)
# @todo agregar validación entre secuencia de las distintas fechas
    fecha_ingreso = models.DateField(default=date.today(),verbose_name=ugettext_lazy(u'Data ingreso'))
    publicado = models.BooleanField(blank=True,verbose_name=ugettext_lazy(u'Publicado'),help_text=ugettext_lazy(u'Indica se o trabalho debe ser publicado no site da agencia'),default=True)

    @staticmethod
    def filter_iniciados(queryset):
      return queryset.filter(estado='IN')

    @staticmethod
    def filter_activos(queryset):
      return queryset.filter(estado='AT')

    def __unicode__(self):
      return _(u'%(titulo)s (%(fecha_ingreso)s)') % {'titulo':self.titulo, 'fecha_ingreso':self.fecha_ingreso}
    class Meta:
      verbose_name = ugettext_lazy(u'Trabalho')
      verbose_name_plural = ugettext_lazy(u"Trabalhos") 
      ordering = ['-fecha_ingreso']
      permissions = (
        ("mail_productora", ugettext_lazy(u'Envio de trabalho por e-mail a produtora')),
        ("mail_agenciados", ugettext_lazy(u'Envio de trabalho por e-mail a agenciados')),
      )

    def thumbnail_img(self):
      url = ''
      if self.thumbnail:
        url = self.thumbnail.url
      return "<img src='%s' height=100 />" % url
    thumbnail_img.allow_tags = True
    thumbnail_img.short_description = ugettext_lazy('Imagem')

    def thumbnail_img_link(self):
      url = ''
      if self.thumbnail:
        url = self.thumbnail.url
      return "<a href='%s'><img src='%s' height=100 /></a>" % (self.imagen.url, url)
    thumbnail_img_link.allow_tags = True
    thumbnail_img_link.short_description = ugettext_lazy(u'Imagem')

    def roles(self):
      roles=self.rol_set.all()
      html = '</ul>'
      for rol in roles:
        html+='<li>%s</li>' % rol.admin_link()
      html += '</ul>'
      return html
    roles.allow_tags = True
    roles.short_description = ugettext_lazy('Perfis')

    def productora_admin_link(self):
      if self.productora.id is None:
        return None
      return u"<a href='/admin/trabajo/productora/%s/'>%s</a>" % (self.productora.id, str(self.productora))
    productora_admin_link.allow_tags=True
    productora_admin_link.short_description = ugettext_lazy(u'Link a produtora')

    def admin_url(self):
      return '/admin/trabajo/trabajo/%s/'%self.id

    def admin_link(self):
      if self.id is None:
        return None
      return u"<a href='%s'>%s</a>" % (self.admin_url(), str(self))
    admin_link.allow_tags=True
    admin_link.short_description = ugettext_lazy(u'Link ao trabalho')

TIPO_EVENTO_TRABAJO=(
  ('C', _(u'Casting')),
  ('B', _(u'Callback')),
  ('P', _(u'Proba de roupa')),
  ('R', _(u'Realização do trabalho')),
  ('O', _(u'Outro')),
)
DICT_TIPO_EVENTO_TRABAJO=dict(TIPO_EVENTO_TRABAJO)

class EventoTrabajo(Evento):
  tipo = models.CharField(max_length=1,choices=TIPO_EVENTO_TRABAJO)
  trabajo = models.ForeignKey(Trabajo,on_delete=models.PROTECT)
  class Meta(Evento.Meta):
    verbose_name = ugettext_lazy(u'Evento do trabalho')
    verbose_name_plural = ugettext_lazy(u'Eventos do trabalho')
  def get_object(self):
    return self.trabajo
  def descripcion_tipo(self):
    return DICT_TIPO_EVENTO_TRABAJO[self.tipo]
  def __unicode__(self):
    return _('%(tipo)s | %(descripcion)s | %(fecha)s | %(direccion)s, %(barrio)s, %(ciudad)s, %(codigo_postal)s') % {
      'tipo':self.descripcion_tipo(), 
      'descripcion':self.descripcion,
      'fecha':self.fecha,
      'direccion':self.direccion,
      'barrio':self.barrio,
      'ciudad':self.ciudad,
      'codigo_postal':self.codigo_postal}


POSTULACION_POR_AGENCIADO='PA'
POSTULADO_PARA_CASTING='PC'
RECHAZO_POSTULACION_CASTING='RP'
SELECCIONADO_PARA_CASTING='SC'
RECHAZO_SELECCION_CASTING='RC'
SELECCIONADO_PARA_CALLBACK='SK'
RECHAZO_SELECCION_CALLBACK='RK'
SELECCIONADO_PARA_TRABAJO='ST'
RECHAZO_SELECCION_TRABAJO='RT'
TRABAJO_REALIZADO='TR'
TRABAJO_NO_REALIZADO='TN'
TRABAJO_PAGADO='TP'

class Rol(models.Model):
    trabajo = models.ForeignKey(Trabajo,on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Descripção'))
    cache = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    caracteristicas = models.TextField(verbose_name=ugettext_lazy(u'Caraterísticas'), null=True, blank=True)
    def __unicode__(self):
      return u'%s (%s)' % (self.descripcion, self.trabajo.titulo)
    class Meta:
      ordering = ['-trabajo__fecha_ingreso','descripcion']
      verbose_name = ugettext_lazy(u"Perfil")
      verbose_name_plural = ugettext_lazy("Perfis") 
      unique_together = (("trabajo", "descripcion"),)

    def cantidad_postulados_casting(self):
      return self.postulacion_set.filter(estado='PC').count()
    cantidad_postulados_casting.short_description = ugettext_lazy(u'Postulados casting')
    def cantidad_seleccionados_casting(self):
      return self.postulacion_set.filter(estado='SC').count()
    cantidad_seleccionados_casting.short_description = ugettext_lazy(u'Selecionados casting')
    def cantidad_seleccionados_trabajo(self):
      return self.postulacion_set.filter(estado='ST').count()
    cantidad_seleccionados_trabajo.short_description = ugettext_lazy(u'Selecionados trabalho')
    def cantidad_trabajos_realizados(self):
      return self.postulacion_set.filter(estado='TR').count()
    cantidad_trabajos_realizados.short_description = ugettext_lazy(u'Trabalhos realizados')
    def cantidad_trabajos_pagados(self):
      return self.postulacion_set.filter(estado='TP').count()
    cantidad_trabajos_pagados.short_description = ugettext_lazy(u'Trabalhos pagados')

    def admin_url(self):
      return '/admin/trabajo/rol/%s/'%self.id

    def admin_link(self):
      if self.id is None:
        return None
      return "<a href='%s'>%s</a>" % (self.admin_url(), str(self))
    admin_link.allow_tags = True
    admin_link.short_description = ugettext_lazy(u'Link ao perfil')

    def trabajo_admin_link(self):
      return self.trabajo.admin_link()
    trabajo_admin_link.allow_tags=True
    trabajo_admin_link.short_description = ugettext_lazy(u'Link ao trabalho')

    def get_postulaciones_confirmables(self):
      return self.postulacion_set.filter(estado__in=[POSTULADO_PARA_CASTING,SELECCIONADO_PARA_CASTING,SELECCIONADO_PARA_TRABAJO])

class EventoRol(Evento):
  tipo = models.CharField(max_length=1,choices=TIPO_EVENTO_TRABAJO)
  rol = models.ForeignKey(Rol,on_delete=models.PROTECT,verbose_name = ugettext_lazy(u'Perfil'))
  class Meta(Evento.Meta):
    verbose_name = ugettext_lazy(u'Evento do perfil')
    verbose_name_plural = ugettext_lazy(u'Eventos do perfil')
  def get_object(self):
    return self.rol
  def descripcion_tipo(self):
    return DICT_TIPO_EVENTO_TRABAJO[self.tipo]
  def __unicode__(self):
    return u'%(tipo)s | %(descripcion)s | %(fecha)s | %(direccion)s, %(barrio)s, %(ciudad)s, %(codigo_postal)s' % {
      'tipo':self.descripcion_tipo(), 
      'descripcion':self.descripcion, 
      'fecha':self.fecha, 
      'direccion':self.direccion, 
      'barrio':self.barrio, 
      'ciudad':self.ciudad,
      'codigo_postal':self.codigo_postal}

class Postulacion(models.Model):
    agenciado = models.ForeignKey(Agenciado,on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol,on_delete=models.PROTECT, verbose_name = ugettext_lazy(u'Perfil'))
    ESTADO_POSTULACION=(
      (POSTULACION_POR_AGENCIADO, _(u'Postulação feita pelo agenciado')),
      (POSTULADO_PARA_CASTING, _(u'Postulado para casting')),
      (RECHAZO_POSTULACION_CASTING,_(u'Postulacion a casting rechazada')),
      (SELECCIONADO_PARA_CASTING, _(u'Selecionado para casting')),
      (RECHAZO_SELECCION_CASTING,_(u'Seleccion a casting rechazada')),
      (SELECCIONADO_PARA_CALLBACK,_(u'Seleccionado para callback')),
      (RECHAZO_SELECCION_CALLBACK,_(u'Seleccion a callback rechazada')),
      (SELECCIONADO_PARA_TRABAJO, _(u'Selecionado para trabalho')),
      (RECHAZO_SELECCION_TRABAJO,_(u'Seleccion a trabajo rechazada')),
      (TRABAJO_REALIZADO, _(u'Trabalho realisado')),
      (TRABAJO_NO_REALIZADO,_(u'Trabajo no realizado')),
      (TRABAJO_PAGADO, _(u'Trabalho pagado')),
    )
    DICT_ESTADO_POSTULACION=dict(ESTADO_POSTULACION)
    estado = models.CharField(max_length=2,choices=ESTADO_POSTULACION,default='PC')
    def __unicode__(self):
      return u'%s | %s | %s' % (self.agenciado,Postulacion.DICT_ESTADO_POSTULACION[self.estado],self.rol)
    class Meta:
      ordering = ['-rol__trabajo__fecha_ingreso', 'rol__descripcion', 'agenciado__nombre', 'agenciado__apellido']
      verbose_name = ugettext_lazy(u'Postulação')
      verbose_name_plural = ugettext_lazy(u"Postulaçoes a trabalhos") 
      unique_together = (("agenciado", "rol"),)

    def trabajo_rol(self):
      return str(self.rol.trabajo)

    def thumbnail_agenciado_link(self):
      return self.agenciado.thumbnail_agenciado_link()
    thumbnail_agenciado_link.allow_tags = True
    thumbnail_agenciado_link.short_description = ugettext_lazy(u'Link ao agenciado')

    def nombre_agenciado(self):
      return self.agenciado.nombre

    def apellido_agenciado(self):
      return self.agenciado.apellido

    def agenciado_admin_link(self):
      if self.agenciado.id is None:
        return ''
      return "<a href='/admin/agencia/agenciado/%s/'>%s</a>" % (self.agenciado.id, self.agenciado)
    agenciado_admin_link.allow_tags = True
    agenciado_admin_link.short_description = ugettext_lazy(u'Link ao agenciado')

    def rol_admin_link(self):
      return self.rol.admin_link()
    rol_admin_link.allow_tags = True
    rol_admin_link.short_description = ugettext_lazy(u'Link ao perfil')

    def descripcion_estado(self):
      return Postulacion.DICT_ESTADO_POSTULACION[self.estado]

    def agenciado_telefonos(self):
      if self.agenciado:
        return self.agenciado.telefonos()
      return None
    agenciado_telefonos.allow_tags = True
    agenciado_telefonos.short_description = ugettext_lazy(u'Telefonos')
