# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.cross.mercadopago.models import MercadoPago
from optparse import make_option

class Command(BaseCommand):

  help=u'Generar toke de acceso'

  def handle(self,*args,**options):

    mp = MercadoPago()

    self.stdout.write(u'Generado token de acceso: %s\n'%mp.get_access_token())

