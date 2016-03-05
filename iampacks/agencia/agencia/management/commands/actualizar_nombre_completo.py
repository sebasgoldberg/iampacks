from django.core.management.base import BaseCommand, CommandError
from iampacks.agencia.agencia.models import Agenciado

class Command(BaseCommand):

  help=u'Actualiza el atributo nombre_completo de todos los agenciados.'

  def actualizar(self):

    for a in Agenciado.objects.all():
      a.save()

  def handle(self,*args,**options):

    self.actualizar()
