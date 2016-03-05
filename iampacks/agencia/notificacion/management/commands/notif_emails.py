# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.models import User
from iampacks.agencia.notificacion.models import NotificacionCuentaAgenciadoExistente

class Command(BaseCommand):

  help=_(u'Notifica a los agenciados que ya tienen cuenta creada y que su email se encuentra en el archivo pasado.')

  option_list = BaseCommand.option_list + (
    make_option('--delay',default=200),
    make_option('--emails', default='emails'),
    )

  def handle(self,*args,**options):

    delay=int(options['delay'])
    emails_file = options['emails']
    with open(emails_file,'r') as f:
      contenido = f.read()

    emails = contenido.split('\n')
    NotificacionCuentaAgenciadoExistente.notificar_emails_listado(emails, delay)
