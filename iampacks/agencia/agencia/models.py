# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from django.conf import settings
from iampacks.agencia.agencia.video import Video
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.cross.direccion.models import Direccion
from iampacks.cross.telefono.models import Telefono as BaseTelefono
from iampacks.agencia.perfil.models import *
from django.contrib import messages
from iampacks.cross.disponibilidad.models import Disponibilidad

# @pre Esta rutina se llama desde el metodo clean de una clase que lo redefine y hereda de formset
def validarUnoIngresado(formset,campo,mensaje):
  if any(formset.errors):
    return
  for form in formset.forms:
    if not campo in form.cleaned_data:
      continue
    if form.cleaned_data[campo] != "":
      if not formset.can_delete: 
        return
      if not form.cleaned_data['DELETE']:
        return
  raise ValidationError(mensaje)

def validarDireccionIngresada(formset):
  validarUnoIngresado(formset,'direccion',_(u'Tem que informar o endereço'))

def validarTelefonoIngresado(formset):
  validarUnoIngresado(formset,'telefono',_(u'Tem que informar um telefone'))

def validarFotoIngresada(formset):
  if Agencia.get_activa().foto_agenciado_obligatoria:
    validarUnoIngresado(formset,'foto',_(u'Tem que subir uma foto'))

class Agencia(models.Model):
  nombre = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Nome'), null=False, blank=False)
  email = models.EmailField(verbose_name=ugettext_lazy(u'e-mail'), null=False, blank=False)
  activa = models.BooleanField(default=True, verbose_name=ugettext_lazy(u'Ativa'),help_text=ugettext_lazy(u'Só debería ter uma unica agencia ativa'))
  logo = models.ImageField(upload_to='agencias/logos/', verbose_name=ugettext_lazy(u'Logo'), help_text = ugettext_lazy(u'Logo a ser visualizado no site da agencia'), null=True, blank=True)
  favicon = models.ImageField(upload_to='agencias/logos/', verbose_name=ugettext_lazy(u'Favicon'), help_text=ugettext_lazy(u'Imagem com extenção ico de 48x48 pixels'), null=True, blank=True)
  titulo_home = models.CharField(max_length=100, verbose_name=ugettext_lazy(u'Titulo pagina inicial'), null=True, blank=True)
  presentacion_home = models.TextField(null=True, blank=True, verbose_name=ugettext_lazy(u'Presentação pagina inicial'))
  mapa_contacto = models.TextField(null=True, blank=True, verbose_name=ugettext_lazy(u'Mapa pagina contato'), help_text=ugettext_lazy(u'Aqui tem que colar o HTML gerado no google maps a partir de seu endereço'))
  foto_agenciado_obligatoria = models.BooleanField(default=True, verbose_name=ugettext_lazy(u'Foto Agenciado Obligatoria'))
  class Meta:
    ordering = ['nombre']
    verbose_name = ugettext_lazy(u"Agencia")
    verbose_name_plural = ugettext_lazy(u"Agencias")

  def __unicode__(self):
    return self.nombre

  def telefonos(self):
    listado_telefonos = []
    for telefono in self.telefonoagencia_set.all():
      listado_telefonos += [telefono.telefono]
    return listado_telefonos

  def direccion(self):
    direcciones = self.direccionagencia_set.all()
    if direcciones:
      return str(direcciones[0])
    return ''

  def get_url_admin(self):
    if self.id:
      return '/admin/agencia/agencia/%s/'%self.id
    return '/admin/agencia/agencia/add/'

  @staticmethod
  def get_activa(request=None):
    agencias = Agencia.objects.filter(activa=True).order_by('-id')
    if not agencias:
      return Agencia(nombre='Agencia',email='mail@agencia.com',activa=False)
    return agencias[0]

class TelefonoAgencia(BaseTelefono):
  agencia = models.ForeignKey(Agencia,null=False, blank=False, verbose_name=ugettext_lazy(u'Agencia'))
  class Meta(BaseTelefono.Meta):
    verbose_name = ugettext_lazy(u"Telefone da Agencia")
    verbose_name_plural = ugettext_lazy(u"Telefones da Agencia")

class DireccionAgencia(Direccion):
  agencia = models.ForeignKey(Agencia,null=False, blank=False, verbose_name=ugettext_lazy(u'Agencia'))
  class Meta(Direccion.Meta):
    verbose_name = ugettext_lazy(u"Endereço da Agencia")
    verbose_name_plural = ugettext_lazy(u"Endereços da Agencia")

def validate_fecha_nacimiento(value):
  if value > date.today():
    raise ValidationError(_(u'A data de nascimento nao pode ser maior que a data do dia'))

def validate_altura(value):
  if value < 15:
    raise ValidationError(_(u'A altura debe ser informada em centimetros'))

class Agenciador(models.Model):

  user= models.OneToOneField(User, null=False, blank=False)

  def __unicode__(self):
    if self.user.name or self.user.lastname:
      return u'%s %s' % (self.user.first_name, self.user.last_name)
    return self.user.username

class Agenciado(models.Model):

    user= models.OneToOneField(User, null=True, blank=True, editable=False, on_delete=models.PROTECT)

    # @todo Ver si se puede quitar null luego de migrar, agregar validacion de que si ya existe que tenga asignado responsable
    # @todo Agregar validación de obligatoriedad cuando no es editado por un agenciador
    mail = models.EmailField(verbose_name=ugettext_lazy(u'e-mail'), null=True, blank=False)

    # Datos personales
    nombre = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Nome'))
    apellido = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Sobrenome'))
    fecha_nacimiento = models.DateField(verbose_name=ugettext_lazy(u'Data nascimento'),validators=[validate_fecha_nacimiento])

    nombre_artistico = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Nombre artístico'), null=True, blank=True)

    # Datos Administrativos
    # @todo Ver si se puede quitar null luego de migrar, agregar validacion de que si ya existe que tenga asignado responsable
    documento_rg = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'RG'))
    # @todo Ver si se puede quitar null luego de migrar, agregar validacion de que si ya existe que tenga asignado responsable
    documento_cpf = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'CPF'),null=True,blank=True)

    documento_drt = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'DRT'),null=True,blank=True)

    responsable = models.CharField(max_length=60, blank=True, verbose_name=ugettext_lazy(u'Responsabel'))
    cuenta_bancaria = models.CharField(max_length=100, blank=True, verbose_name=ugettext_lazy(u'Conta bancaria'))

    """
    # Datos de direccion
    estado = models.ForeignKey(Estado,on_delete=models.PROTECT,null=True, blank=False, verbose_name=ugettext_lazy(u'Estado'))
    ciudad = models.ForeignKey(Ciudad,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Cidade'),null=True, blank=False)
    barrio = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Barrio'))
    direccion = models.CharField(max_length=120, verbose_name=ugettext_lazy(u'Endereço'))
    codigo_postal = models.CharField(max_length=40, verbose_name=ugettext_lazy(u'CEP'))
    """

    # Caracteristicas fisicas
    SEXO=(
      ('M', _(u'Masculino')),
      ('F', _(u'Feminino')),
    )
    DICT_SEXO=dict(SEXO)
    sexo = models.CharField(max_length=1,choices=SEXO, verbose_name=ugettext_lazy(u'Sexo'))
    ojos = models.ForeignKey(Ojos,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Olhos'),null=True, blank=False)
    pelo = models.ForeignKey(Pelo,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Cabelo'),null=True, blank=False)
    piel = models.ForeignKey(Piel,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Pele'),null=True, blank=False)
    altura = models.FloatField(verbose_name=ugettext_lazy(u'Altura (cm)'),validators=[validate_altura])
    peso = models.FloatField(verbose_name=ugettext_lazy(u'Peso (kg)'))
    talle = models.ForeignKey(Talle,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Manequim'),null=True, blank=False)

    talle_camisa = models.IntegerField(verbose_name=ugettext_lazy(u'Camisa'))
    talle_pantalon = models.IntegerField(verbose_name=ugettext_lazy(u'Calça'))

    talle_ropa_camisa = models.ForeignKey(TalleRopa,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Camisa'),null=True, blank=True, related_name='camisa')
    talle_ropa_pantalon = models.ForeignKey(TalleRopa,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Calça'),null=True, blank=True,related_name='pantalon')

    calzado = models.IntegerField(verbose_name=ugettext_lazy(u'Calçado'))
    estado_dientes = models.ForeignKey(EstadoDientes,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Estado Dentes'),null=True, blank=False)

    # Habilidades
    deportes = models.ManyToManyField(Deporte, blank=True, verbose_name=ugettext_lazy(u'Esportes'))
    danzas = models.ManyToManyField(Danza, blank=True, verbose_name=ugettext_lazy(u"Danças"))
    instrumentos = models.ManyToManyField(Instrumento, blank=True, verbose_name=ugettext_lazy(u'Instrumentos'))
    idiomas = models.ManyToManyField(Idioma, blank=True, verbose_name=ugettext_lazy(u'Idiomas'))
    indicador_maneja = models.BooleanField(verbose_name=ugettext_lazy(u'Dirige'))
    indicador_tiene_registro = models.BooleanField(verbose_name=ugettext_lazy(u'Habilitação'))

    # Otros datos
    trabaja_como_extra = models.BooleanField(verbose_name=ugettext_lazy(u'Faz figuração'))
    como_nos_conocio = models.TextField(blank=True, verbose_name=ugettext_lazy(u'Como nos conheceu'))
    observaciones = models.TextField(blank=True, verbose_name=ugettext_lazy(u'Observaçoes'))

    # Datos administrativos del sistema 
    activo = models.BooleanField(default=True, verbose_name=ugettext_lazy(u'Ativo'))
    fecha_ingreso = models.DateField(default=date.today(), verbose_name=ugettext_lazy(u'Data de agenciamento'))
    recurso_id = models.IntegerField(null=True, editable=False) #Clave en aplicacion DELPHI

    # Agenciador 
    referente=models.OneToOneField(Agenciador, null=True, blank=True)
    nombre_completo = models.CharField(max_length=121, null=False, editable=False)
    
    def __unicode__(self):
      return u'%s %s (%s)' % (self.nombre, self.apellido, self.fecha_nacimiento)

    def save(self, *args, **kwargs):
      self.nombre_completo = '%s %s'%(self.nombre,self.apellido)
      super(Agenciado, self).save(*args, **kwargs)

    def thumbnail(self):
      url = ''
      if any(self.fotoagenciado_set.order_by('id')):
        url = self.fotoagenciado_set.order_by('id')[:1][0].thumbnail.url
      return "<img src='%s' height=100 />" % url
    thumbnail.allow_tags = True
    thumbnail.short_description = ugettext_lazy(u'Imagem')

    def thumbnail_url(self):
      url = ''
      if any(self.fotoagenciado_set.order_by('id')):
        url = self.fotoagenciado_set.order_by('id')[:1][0].thumbnail.url
      return url

    def thumbnails(self):
      html=''
      fotos=self.fotoagenciado_set.order_by('id')
      for foto in fotos:
        url = foto.foto.url
        url_thumbnail = foto.thumbnail.url
        html = html + "<a href='%s'><img src='%s' height=100 /></a>" % (url,url_thumbnail)
      return html
    thumbnails.allow_tags = True
    thumbnails.short_description = ugettext_lazy(u'Imagems')

    def thumbnails_absolute_uri(self):
      html=''
      fotos=self.fotoagenciado_set.order_by('id')
      for foto in fotos:
        url = "%s%s" % (settings.AMBIENTE.get_base_url(), foto.foto.url)
        url_thumbnail = "%s%s" % (settings.AMBIENTE.get_base_url(), foto.thumbnail.url)
        html = html + "<a href='%s'><img src='%s' height=100 /></a>" % (url,url_thumbnail)
      return html
    thumbnails_absolute_uri.allow_tags = True
    thumbnails_absolute_uri.short_description = ugettext_lazy(u'Imagems')

    def thumbnail_agenciado_link(self):
      return "<a href='/admin/agencia/agenciado/%s/'>%s</a>" % (str(self.id),self.thumbnail())
    thumbnail_agenciado_link.allow_tags = True
    thumbnail_agenciado_link.short_description = ugettext_lazy(u'Link ao agenciado')

    def html_small_youtube_iframes(self):
      html=''
      for video in self.videoagenciado_set.all():
        html="%s %s"%(html,video.html_small_youtube_iframe())
      return html
    html_small_youtube_iframes.allow_tags = True
    html_small_youtube_iframes.short_description = ugettext_lazy(u'Video')

    def telefonos(self):
      listadoTelefonos=[]
      for telefono in self.telefono_set.all():
        if telefono.compania is not None:
          listadoTelefonos.append('%s: %s' % (telefono.compania, telefono.telefono))
        else:
          listadoTelefonos.append(telefono.telefono)
      return '<br />'.join(listadoTelefonos)
    telefonos.allow_tags = True
    telefonos.short_description = ugettext_lazy(u'Telefones')

    def admin_link(self):
      if self is None:
        return ''
      return "<a href='/admin/agencia/agenciado/%s/'>%s</a>" % (self.id,self)
    admin_link.allow_tags=True
    admin_link.short_description = ugettext_lazy(u'Link ao agenciado')

    def descripcion(self):
      return _(u'Edad %(edad)s, sexo %(sexo)s, olhos %(ojos)s, cabelo %(pelo)s, pele %(piel)s, altura %(altura)s, peso %(peso)s, estado dentes %(estado_dientes)s.')%{'edad':self.edad(), 'sexo':Agenciado.DICT_SEXO[self.sexo], 'ojos':self.ojos, 'pelo':self.pelo, 'piel':self.piel, 'altura':self.altura, 'peso':self.peso, 'estado_dientes':self.estado_dientes}
    descripcion.short_description = ugettext_lazy(u'Descripção')

    def edad(self):
      dias_desde_nacimiento=(date.today()-self.fecha_nacimiento).days
      if dias_desde_nacimiento<365:
        return _(u'%s meses')%int(dias_desde_nacimiento/30.4375)
      return _(u'%s anos')%int(dias_desde_nacimiento/365.25)
    edad.short_description = ugettext_lazy(u'Edad')

    def ids_roles_postulaciones(self):
      return [ postulacion.rol.id for postulacion in self.postulacion_set.all() ]

    def get_mails(self):
      if self.mail:
        listadoMails=[self.mail]
      else:
        listadoMails=[]
      for mail in self.mailagenciado_set.all():
        listadoMails.append(u'%s'%mail)
      return listadoMails
      
    def mails(self):
      return '<br />'.join(self.get_mails())
    mails.allow_tags = True
    mails.short_description = ugettext_lazy(u'Mails')

    @staticmethod
    def autocomplete_search_fields():
      return ("id__iexact", "nombre_completo__icontains",)

    class Meta:
      ordering = ['nombre', 'apellido']
      verbose_name = ugettext_lazy(u"Agenciado")
      verbose_name_plural = ugettext_lazy(u"Agenciados")

class MailAgenciado(models.Model):
  agenciado = models.ForeignKey(Agenciado)
  email = models.EmailField(verbose_name=ugettext_lazy(u'e-mail'), null=False , blank=False)
  descripcion = models.CharField(max_length=100, verbose_name=ugettext_lazy(u'Descripção'), null=True, blank=True)
  def __unicode__(self):
    if self.descripcion:
      return u'%s (%s)' % (self.email, self.descripcion)
    return u'%s' % self.email
  class Meta:
    verbose_name = ugettext_lazy(u"Mail Agenciado")
    verbose_name_plural = ugettext_lazy(u"Mails Agenciado")

class DireccionAgenciado(Direccion):
  agenciado = models.ForeignKey(Agenciado, verbose_name=ugettext_lazy(u'Agenciado'))
  class Meta(Direccion.Meta):
    verbose_name = ugettext_lazy(u"Endereço agenciado")
    verbose_name_plural = ugettext_lazy(u"Endereços agenciados")

MAX_FOTO_SIZE = 1
def validate_image(fieldfile_obj):
  filesize = fieldfile_obj.file.size
  if filesize >= MAX_FOTO_SIZE*1024*1024: 
    raise ValidationError(_(u"Por favor subir archivos con tamaño menor a %s MB") % str(MAX_FOTO_SIZE))

class FotoAgenciado(models.Model):
    agenciado = models.ForeignKey(Agenciado)
    foto = models.ImageField(verbose_name=ugettext_lazy(u'Foto (tamaño < %s MB)') % MAX_FOTO_SIZE, upload_to='agenciados/fotos/', blank=True, validators=[validate_image])
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)], source='foto', format='JPEG', options={'quality': 90})
    mini_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60,60)], source='foto', format='JPEG', options={'quality': 90})
    def __unicode__(self):
      return self.foto.url
    class Meta:
      verbose_name = ugettext_lazy(u"Foto agenciado")
      verbose_name_plural = ugettext_lazy(u"Fotos agenciado")


class VideoAgenciado(Video):
  agenciado = models.ForeignKey(Agenciado)
  class Meta(Video.Meta):
    verbose_name = ugettext_lazy(u"Video agenciado")
    verbose_name_plural = ugettext_lazy(u"Videos agenciado")

@receiver(pre_save, sender=VideoAgenciado)
def callback_pre_save_videoagenciado(sender, instance, raw, using, **kwargs):
  instance.url_to_codigo_video()

class Telefono(BaseTelefono):
  agenciado = models.ForeignKey(Agenciado)

  class Meta(BaseTelefono.Meta):
    verbose_name = ugettext_lazy(u"Telefone agenciado")
    verbose_name_plural = ugettext_lazy(u"Telefones agenciado")

class DisponibilidadTrabajoAgenciado(Disponibilidad):
  agenciado = models.ForeignKey(Agenciado)
  class Meta(Disponibilidad.Meta):
    verbose_name = ugettext_lazy(u"Disponibilidad Trabajo")
    verbose_name_plural = ugettext_lazy(u"Disponibilidades Trabajo")

class TrabajoVigente(models.Model):
  descripcion = models.CharField(max_length=100, verbose_name=ugettext_lazy(u'Descripción'))
  fecha_vigencia = models.DateField(verbose_name=ugettext_lazy(u'Fecha vigencia'))

  def clean(self):
    if not self.id:
      if self.fecha_vigencia:
        if self.fecha_vigencia <= date.today():
          raise ValidationError(_(u'La fecha de vigencia debe ser posterior a la fecha actual.'))

  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u"Trabajo vigente")
    verbose_name_plural = ugettext_lazy(u"Trabajos vigentes")

class TrabajoVigenteAgenciado(TrabajoVigente):
  agenciado = models.ForeignKey(Agenciado)
  class Meta(TrabajoVigente.Meta):
    verbose_name = ugettext_lazy(u"Trabajo vigente")
    verbose_name_plural = ugettext_lazy(u"Trabajos vigentes")

class TrabajoRealizado(models.Model):
  descripcion = models.CharField(max_length=100, verbose_name=ugettext_lazy(u'Descripción'))
  fecha_desde = models.DateField(verbose_name=ugettext_lazy(u'Fecha desde'))
  fecha_hasta = models.DateField(verbose_name=ugettext_lazy(u'Fecha hasta'), null=False, blank=False)

  def clean(self):
    if self.fecha_hasta:
      if self.fecha_desde:
        if self.fecha_desde >= self.fecha_hasta:
          raise ValidationError(_(u'La fecha desde debe ser menor a la fecha hasta.'))

  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u"Trabajo realizado")
    verbose_name_plural = ugettext_lazy(u"Trabajos realizados")

class TrabajoRealizadoAgenciado(TrabajoRealizado):
  agenciado = models.ForeignKey(Agenciado)
  class Meta(TrabajoRealizado.Meta):
    verbose_name = ugettext_lazy(u"Trabajo realizado")
    verbose_name_plural = ugettext_lazy(u"Trabajos realizados")
