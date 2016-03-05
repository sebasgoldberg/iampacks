from django.core.management.base import BaseCommand, CommandError
from iampacks.agencia.agencia.models import Agenciado, DireccionAgenciado
from cities_light.models import City, Region, Country
from django.conf import settings

class Command(BaseCommand):

  help=u'Verifica si las ciudades del modelo agencia.models.Ciudad existen en las ciudades del modelo cities_light.models.City'

  def handle(self,*args,**options):

    brasil=Country.objects.get(code2='BR')
    cantidad_agenciados_sin_migrar = 0

    for agenciado in Agenciado.objects.all():
      if not agenciado.direccionagenciado_set.all():

        region = None
        if agenciado.estado:
          try:
            region = Region.objects.get(country=brasil,name=agenciado.estado.descripcion)
          except Region.DoesNotExist:
            pass

        city = None
        if agenciado.ciudad:
          try:
            if region:
              city = City.objects.get(region=region,name=agenciado.ciudad.descripcion)
            else:
              city = City.objects.get(region__country=brasil,name=agenciado.ciudad.descripcion)
              region = city.region
          except City.DoesNotExist:
            pass

        direccion=DireccionAgenciado(
          agenciado=agenciado,
          pais=brasil,
          estado=region,
          ciudad=city,
          barrio=agenciado.barrio,
          direccion=agenciado.direccion,
          codigo_postal=agenciado.codigo_postal
          )
        direccion.save()
        
    self.stdout.write('No se han podido migrar %s agenciado.\n'%cantidad_agenciados_sin_migrar)
