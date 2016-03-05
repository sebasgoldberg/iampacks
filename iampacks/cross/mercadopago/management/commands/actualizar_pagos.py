# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.cross.mercadopago.models import MercadoPago
from optparse import make_option

class Command(BaseCommand):

  help=u'Obtiene la información de un pago'

  option_list = BaseCommand.option_list + (
    make_option('--id_pago'),
    make_option('--ext_ref'),
    )


  def handle(self,*args,**options):
    
    mp = MercadoPago()

    id_pago=options['id_pago']
    ext_ref=options['ext_ref']

    if id_pago:
      self.stdout.write(u'Se obtendrá información para el pago con id %s.\n'%id_pago)
      infopago=mp.get_pago(id_pago)
    elif ext_ref:
      self.stdout.write(u'Se obtendrá información para el pago con referencia externa %s.\n'%ext_ref)
      infopago=mp.search_pagos_by_external_reference(ext_ref)
    else:
      raise Exception('Debe pasar como parámetro el id del pago o su referencia externa.')

    self.stdout.write(u'Informacion del pago: %s\n'%infopago)

