# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.cross.mercadopago.models import MercadoPago, Pago
from optparse import make_option
import pprint

class Command(BaseCommand):

  help=u'Obtiene la información de un pago'

  option_list = BaseCommand.option_list + (
    make_option('--id_pago'),
    make_option('--ext_ref'),
    make_option('--approved_and_accredited', action='store_true', default=False),
    )


  def handle(self,*args,**options):
    
    mp = MercadoPago()

    id_pago=options['id_pago']
    ext_ref=options['ext_ref']
    approved_and_accredited=options['approved_and_accredited']

    if id_pago:
      self.stdout.write(u'Se obtendrá información para el pago con id %s.\n'%id_pago)
      infopago=mp.get_pago(id_pago)
    elif ext_ref:
      if approved_and_accredited:
        pago=Pago.objects.get(pk=ext_ref)
        if pago.approved_and_accredited():
          self.stdout.write(u'El pago esta aprovado y acreditado.\n')
        else:
          self.stdout.write(u'El pago NO esta aprovado y acreditado.\n')
        return
      self.stdout.write(u'Se obtendrá información para el pago con referencia externa %s.\n'%ext_ref)
      infopago=mp.search_pagos_by_external_reference(ext_ref)
    else:
      self.stdout.write(u'Se obtienen todos los pagos.\n')
      infopago=mp.get_pagos()

    pp=pprint.PrettyPrinter(indent=2)
    self.stdout.write(u'Informacion del pago: %s\n'%pp.pformat(infopago))

