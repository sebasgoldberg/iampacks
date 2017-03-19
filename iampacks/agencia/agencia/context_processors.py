from iampacks.agencia.agencia.models import FotoAgenciado, Agencia

class ThumbnailsUrls(object):


  def __init__(self, max_cantidad_thumbnails = 17):
    self.arriba = []
    self.abajo = []
    todos = FotoAgenciado.objects.filter(agenciado__activo=True).order_by('?')
    for imagen_agenciado in todos:
      try:
        if len(self.arriba)<max_cantidad_thumbnails:
          self.arriba.append(imagen_agenciado.mini_thumbnail.url)
        else:
          self.abajo.append(imagen_agenciado.mini_thumbnail.url)
      except:
        pass
      if len(self.abajo)==max_cantidad_thumbnails:
        break
    if len(self.abajo)<max_cantidad_thumbnails:
      self.abajo=self.arriba

def thumbnails_urls(request):
  """
  Devuelve 10 agenciados al azar que contengan al menos un thumbnai
  """
  return {'thumbnails_urls': ThumbnailsUrls()}

def agencia(request):
  """
  Devuelve la agencia activa
  """
  return {'agencia':Agencia.get_activa(request)}
