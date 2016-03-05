# coding=utf-8
from django.test import TestCase
from iampacks.agencia.notificacion.models import NotificacionCuentaAgenciadoExistente
from django.core import mail
from iampacks.agencia.agencia.models import Agenciado
from django.contrib.auth.models import User
import StringIO

class NotificacionCuentaAgenciadoExistenteTestCase(TestCase):

  fixtures = [u'fixture/test/agencia.json']

  def test_notificacion_enviada(self):


    # Se verifica que se creen correctamente los usuarios.
    agenciados_sin_usuario = Agenciado.objects.filter(mail__isnull=False,user__isnull=True)
    cantidad_agenciados_sin_usuario = agenciados_sin_usuario.count()
    agenciado = agenciados_sin_usuario.first()
    NotificacionCuentaAgenciadoExistente.crear_usuario_agenciado(agenciado,'testtest')
    self.assertNotEqual(agenciado.user.id, None)
    Agenciado.objects.get(user=agenciado.user)
    self.assertFalse(agenciado.user.is_staff)
    self.assertFalse(agenciado.user.is_superuser)
    self.assertTrue(agenciado.user.last_login,None)
    self.assertEquals(cantidad_agenciados_sin_usuario-1,Agenciado.objects.filter(mail__isnull=False,user__isnull=True).count())


    # Se verifica correcta notificacion y creación de usuarios
    cantidad_agenciados = Agenciado.objects.filter(mail__isnull=False).count()
    self.assertGreater(cantidad_agenciados, 0)

    agenciados_sin_usuario = Agenciado.objects.filter(mail__isnull=False,user__isnull=True)

    cantidad_agenciados_sin_usuario = agenciados_sin_usuario.count()
    self.assertGreater(cantidad_agenciados_sin_usuario, 0)

    cantidad_mails_a_enviar = 0
    for a in agenciados_sin_usuario:
      cantidad_mails_a_enviar += len(a.get_mails())

    NotificacionCuentaAgenciadoExistente.notificar_no_notificados()

    self.assertEquals(len(mail.outbox), cantidad_mails_a_enviar)
    self.assertEquals(len(Agenciado.objects.filter(mail__isnull=False,user__isnull=True)), 0)

    # Se verifica que no se vuelvan a notificar los ya notificados.
    NotificacionCuentaAgenciadoExistente.notificar_no_notificados()

    self.assertEquals(len(mail.outbox), cantidad_mails_a_enviar)
    self.assertEquals(len(Agenciado.objects.filter(user__isnull=True)), 0)


class NotificacionAgenciadoConUsuario(TestCase):

  fixtures = [u'fixture/test/agencia.json']

  def test_notificacion_enviada(self):

    # Se verifica que se creen correctamente los usuarios.
    agenciados_con_usuario_y_mail = Agenciado.objects.filter(mail__isnull=False,user__isnull=False)
    self.assertGreater(agenciados_con_usuario_y_mail.count(),0)

    cantidad_mails_a_enviar = 0
    mails = []
    for a in agenciados_con_usuario_y_mail:
      mails += a.get_mails()
      cantidad_mails_a_enviar += len(a.get_mails())

    NotificacionCuentaAgenciadoExistente.notificar_emails_listado(mails)
    self.assertEquals(len(mail.outbox), cantidad_mails_a_enviar)

    # Se verifica que si repetimos la operación entonces el resultado es el mismo.
    NotificacionCuentaAgenciadoExistente.notificar_emails_listado(mails)
    self.assertEquals(len(mail.outbox), 2*cantidad_mails_a_enviar)
