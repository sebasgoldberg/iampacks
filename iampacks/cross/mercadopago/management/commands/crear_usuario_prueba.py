# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.cross.mercadopago.models import MercadoPago
from optparse import make_option

class Command(BaseCommand):

  help=u'Crear un usuario de prueba en mercadopago'

  option_list = BaseCommand.option_list + (
    make_option('--site_id', default=u'MLA'),
    )


  def handle(self,*args,**options):

    site_id=options['site_id']

    mp = MercadoPago()

    self.stdout.write(u'Se creará usuario de prueba para el site_id: %s\n'%site_id)

    datos_usuario_prueba=mp.crear_usuario_prueba(site_id)

    self.stdout.write(u'Se ha creado usuario de prueba con los siguientes datos: %s\n'%datos_usuario_prueba)
