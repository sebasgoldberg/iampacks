# coding=utf-8
from django.db import models
from django.template import loader, Context
from iampacks.agencia.agencia.models import Agencia, Agenciado, MailAgenciado
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.agencia.agencia.mail import MailAgencia
from django.conf import settings
from django.contrib.auth.models import User
import datetime
import time
import re
from django.core.exceptions import ValidationError

class BaseNotificacionMail(models.Model):

  email_destinatario = models.EmailField(verbose_name=ugettext_lazy(u'e-mail destinatario'), null=True, blank=False)
  fecha_envio = models.DateTimeField(verbose_name=ugettext_lazy(u'Fecha de envío'), default=datetime.datetime.now())

  class Meta:
    abstract = True

  def get_template_name(self):
    raise Exception(u'Método no implementado')

  def get_context_dict(self):
    raise Exception(u'Método no implementado')

  def get_notification_title(self):
    raise Exception(u'Método no implementado')

  def get_ccs(self):
    return [agencia.email]

  def enviar(self):

    template = loader.get_template(self.get_template_name())
    context = Context(self.get_context_dict())
    asunto = self.get_notification_title()
    destinatarios = [self.email_destinatario]
    agencia=Agencia.get_activa()
    ccs = self.get_ccs()

    text_content = _(u'Este mensagem deve ser visualizado em formato HTML.')
    html_content = template.render(context)
    msg = MailAgencia(asunto, text_content, destinatarios,ccs=ccs)
    msg.set_html_body(html_content)
    msg.send()

    self.fecha_envio = datetime.datetime.now()
    self.clean()
    self.save()

class NotificacionCuentaAgenciadoExistente(BaseNotificacionMail):

  agenciado = models.ForeignKey(Agenciado)
  password = None

  def get_template_name(self):
    return 'notificacion/cuenta_agenciado_existe.html'

  def get_context_dict(self):
    return {'agenciado': self.agenciado,
      'ambiente': settings.AMBIENTE, 
      'password': self.password,
      'agencia': Agencia.get_activa()}

  def get_notification_title(self):
    return _(u'Você Está Cadastrado')

  def get_ccs(self):
    return []

  @staticmethod
  def crear_usuario_agenciado(agenciado, password):
    agenciado.user = User.objects.create_user(agenciado.mail[:30], agenciado.mail, password)
    agenciado.user.first_name = agenciado.nombre[:30]
    agenciado.user.last_name = agenciado.apellido[:30]
    agenciado.user.is_active = True
    agenciado.user.save()
    agenciado.save()

  @staticmethod
  def notificar_agenciado(agenciado, password, delay):

    for mail in agenciado.get_mails():
      try:

        notificacion = NotificacionCuentaAgenciadoExistente(
          email_destinatario=mail, agenciado=agenciado)
        notificacion.password = password
        notificacion.enviar()
        if delay:
          time.sleep(delay)

      except:
        pass

  @staticmethod
  def notificar_no_notificados(delay=None):

    agenciados = Agenciado.objects.filter(mail__isnull=False,user__isnull=True)

    for agenciado in agenciados:

      if not agenciado.mail:
        continue
      if agenciado.user:
        continue
    
      password = User.objects.make_random_password()

      try:

        NotificacionCuentaAgenciadoExistente.crear_usuario_agenciado(
          agenciado,password)

        NotificacionCuentaAgenciadoExistente.notificar_agenciado(
          agenciado,password, delay)

      except:
        pass

   
  @staticmethod
  def notificar_emails_listado(emails, delay=None):
    """
    Se notifica a agenciados que tienen usuario asignado y que alguno
    de sus mails se encuentra dentro del listado.
    """

    ids_agenciados = set([a.id for a in Agenciado.objects.filter(
      mail__in=emails,user__isnull=False) ])
    ids_agenciados = ids_agenciados | set(
      ma.agenciado.id for ma in MailAgenciado.objects.filter(
        email__in=emails,agenciado__user__isnull=False))

    for agenciado in Agenciado.objects.filter(id__in=ids_agenciados):

      password = User.objects.make_random_password()
      user = agenciado.user
      user.set_password(password)
      user.save()

      NotificacionCuentaAgenciadoExistente.notificar_agenciado(
        agenciado, password, delay)

class MailInvalido(models.Model):

  email = models.EmailField(verbose_name=ugettext_lazy(u'e-mail'), null=False, blank=False, unique=True)
  fecha_deteccion = models.DateTimeField(verbose_name=ugettext_lazy(u'Fecha de detección'), default=datetime.datetime.now())

  def get_agenciados(self):
    agenciados = set(Agenciado.objects.filter(mail=self.email))
    agenciados = agenciados | set(
      [ma.agenciado for ma in MailAgenciado.objects.filter(
        email=self.email)])
    return agenciados

  def links_agenciados(self):
    agenciados = self.get_agenciados()
    result=''
    for a in agenciados:
      result=result + '<li>%s</li>' % a.admin_link()
    return '<ul>%s</ul>' % result
  links_agenciados.allow_tags=True
  links_agenciados.short_description = ugettext_lazy(u'Link aos agenciados')

  def clean(self):
    raise ValidationError(ugettext_lazy(u'Sin permisos para modificar'))
