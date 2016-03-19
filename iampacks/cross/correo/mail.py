# coding=utf-8
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from iampacks.cross.correo import settings as correo_settings

class Mail(EmailMultiAlternatives):

  def actualizar_asunto(self,asunto):
    return asunto

  def get_reply_to(self):
    return None

  def __init__(self,asunto, cuerpo_de_texto, destinatarios,ccs=None,bccs=None):

    if correo_settings.EMAIL_USER is None:
      # @todo Ver de loguear el un warning.
      pass
      #raise Exception(u'No se ha definido configuración para EMAIL_USER (remitente de emails)')
    
    _asunto = self.actualizar_asunto(asunto)
    reply_to=self.get_reply_to()
    if reply_to:
      _headers = {'Reply-To': reply_to}
    else:
      _headers = {}
    
    self.mensaje = EmailMultiAlternatives(
      _asunto,
      cuerpo_de_texto,
      correo_settings.EMAIL_USER,
      destinatarios,
      headers = _headers,
      cc=ccs,
      bcc=bccs
    )

  def set_html_body(self,html_content):
    self.mensaje.attach_alternative(html_content, "text/html")

  def send(self):
    from socket import error as socket_error
    try:
      self.mensaje.send()
    except socket_error as e:
      # @todo Ver de loguear el error.
      pass

  @staticmethod
  def get_email_admins():
    """
    Obtiene un lista con los emails de los administradores definidos 
    en settings.
    """
    return [ mail for _, mail in settings.ADMINS ]

