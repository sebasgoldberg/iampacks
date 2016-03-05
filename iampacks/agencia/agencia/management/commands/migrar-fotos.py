from django.core.management.base import BaseCommand, CommandError
from iampacks.agencia.agencia.models import Agenciado, FotoAgenciado, VideoAgenciado, Compania, Telefono
from iampacks.agencia.perfil.models import Danza, Deporte, EstadoDientes, Idioma, Instrumento, Ojos, Pelo, Piel, Talle
import pymssql
from django.core.files.images import ImageFile
import os
from django.conf import settings

class Command(BaseCommand):

  help=u'Migra las fotos en una ruta determinada de los recursos DELPHI a los agenciados'

  # Migra cada foto para el agenciado pasado
  # @pre La foto del agenciado se encuentra en carpeta self.origenFotos, con el siguiente nombre:
  #   <imagen_recurso.id>.jpg
  # De forma que el path absoluto sera 
  #   self.origenFotos/<imagen_recurso.id>.jpg
  # El contenido de la foto sera la correspondiente al campo imagen_recurso.imagen para el
  # id encontrado en el nombre.
  # @pre el agenciado pasado contendra el campo recurso_id y se correspondera con el de la
  # aplicacion DELPHI
  def migrarFotos(self,agenciado):
    
    if not agenciado.recurso_id:
      return

    cursor=self.connection.cursor()

    cursor.execute(
      'select id, imagen '+
      'from imagen_recurso '+
      'where recurso_id = '+str(agenciado.recurso_id)
    )

    for row in cursor:

      filename=str(row['id'])+'.tmp.jpg'

      f=open(filename,'wb')

      f.write(row['imagen'])

      f.close()

      f=open(filename,'rb')
      imageFile=ImageFile(f)

      fa=agenciado.fotoagenciado_set.create( )
      fa.foto.save(filename,imageFile,save=True)

      self.stdout.write('Foto agregada al agenciado %s\n'%agenciado)
      f.close()
      
      os.remove(filename)

  def handle(self,*args,**options):

    self.connection = pymssql.connect(host=settings.AMBIENTE.mssqlserver.host, user='aretha', password='aretha01', database='alternativa', as_dict=True)

    cursor = self.connection.cursor()
    
    agenciados = Agenciado.objects.all()

    for agenciado in agenciados:
      self.migrarFotos(agenciado)

    self.connection.close()

