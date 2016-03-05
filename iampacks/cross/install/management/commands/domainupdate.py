from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from iampacks.cross.zonomi.models import Zonomi

class Command(BaseCommand):

  help=u'Instala la agencia y la deja lista para usar.'

  def get_dominio(self):
    return settings.AMBIENTE.dominio

  def set_ddns_updater(self):

    if settings.AMBIENTE.zonomi.api_key:
      ddns = Zonomi(settings.AMBIENTE.zonomi.api_key)
      ddns.domain_update(self.get_dominio())

  def handle(self,*args,**options):

    self.set_ddns_updater()

    self.stdout.write('Dominio agregado.\n')

