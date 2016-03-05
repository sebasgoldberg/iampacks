# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.models import User
from iampacks.agencia.notificacion.models import NotificacionCuentaAgenciadoExistente

class Command(BaseCommand):

  help=_(u'Notifica a los agenciados que no tienen cuenta creada que ya pueden acceder a su cuenta.')

  option_list = BaseCommand.option_list + (
    make_option('--delay',default=200),
    )

  def handle(self,*args,**options):

    delay=options['delay']
    
    NotificacionCuentaAgenciadoExistente.notificar_no_notificados(delay)
