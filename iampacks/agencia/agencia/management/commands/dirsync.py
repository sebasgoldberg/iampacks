# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.agencia.agencia.models import DireccionAgencia, DireccionAgenciado
from iampacks.agencia.trabajo.models import DireccionProductora, EventoTrabajo, EventoRol
from cities_light.models import City, Region

class Command(BaseCommand):

  help=u'Sincroniza la region en función de la ciudad y el país en función de la región'

  def dirsync(self,direccion):
    
    try:
      if direccion.ciudad:
        direccion.estado = direccion.ciudad.region
        self.stdout.write('Asignado estado %s en funcion de ciudad %s.\n'%(direccion.estado,direccion.ciudad))
    except City.DoesNotExist:
      direccion.ciudad=None

    try:
      if direccion.estado:
        direccion.pais = direccion.estado.country
        self.stdout.write('Asignado pais %s en funcion de estado %s.\n'%(direccion.estado,direccion.ciudad))
    except Region.DoesNotExist:
      direccion.estado=None
      direccion.pais=None
    

    direccion.save()

  def dirmodelsync(self,model):
    self.stdout.write('Se sincroniza el modelo %s\n'%model)
    for direccion in model.objects.all():
      self.dirsync(direccion)

  def handle(self,*args,**options):
    self.dirmodelsync(DireccionAgencia)
    self.dirmodelsync(DireccionAgenciado)
    self.dirmodelsync(DireccionProductora)
    self.dirmodelsync(EventoTrabajo)
    self.dirmodelsync(EventoRol)


