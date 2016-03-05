from iampacks.agencia.agencia.models import Agencia
from django.shortcuts import redirect

PATH_CREACION_AGENCIA = (
  '/admin/agencia/agencia/add/',
  '/admin/agencia/agencia/add/',
  )

PATH_EXCEPCIONES = (
  '/admin/logout/',
  '/usuario/logout/',
  )

class AgenciaMiddleware:
  
  def process_request(self, request):
    if Agencia.get_activa().activa:
      return None
    if request.path in PATH_CREACION_AGENCIA:
      return None
    if request.path in PATH_EXCEPCIONES:
      return None
    if len(Agencia.objects.all()) == 0:
      return redirect('/admin/agencia/agencia/add/')
    edit_path= '/admin/agencia/agencia/%s/' % Agencia.objects.first().id
    if edit_path == request.path:
      return None
    return redirect(edit_path)
