# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from iampacks.agencia.agencia.tests import AgenciaTestCase
from django.test.client import Client
from iampacks.agencia.agencia.models import Agenciado

from django.contrib.auth.models import User
from django.core import mail

class TrabajoTestCase(TestCase):

  fixtures = [
    'trabajo/fixtures/agenciador_user.yaml',
    'agencia/fixtures/test-data.yaml'
  ]

  @staticmethod
  def get_management_form_data(setname=u'<model>_set'):
    return {
      setname+'-TOTAL_FORMS': u'1',
      setname+'-INITIAL_FORMS': u'0',
      setname+'-MAX_NUM_FORMS': u'',
    }


  def test_postulaciones(self):
    """
    Test de funcionalidad agregada en la administración para postulaciones 
    masivas y envio de trabajos por mail.
    """

    """
    Login de usuario agenciador
    """
    c = Client()
    self.assertTrue(c.login(username = 'agenciadortest', password = 'Inicial01'))
    
    """
    Se ingresa a la administración y luego a la creación de agenciados
    """
    response = c.get('/admin/')
    self.assertEqual(response.status_code,200)
    response = c.get('/admin/agencia/agenciado/add/')
    self.assertEqual(response.status_code,200)

    """
    Se intenta crear el agenciado
    """
    dict_form_agenciado = AgenciaTestCase.get_dict_form_agenciado(mail=u'testtrabajo01@gmail.com',rg=u'123100-2-01',cpf=u'123100-2-01')
    dict_form_agenciado.update(TrabajoTestCase.get_management_form_data('postulacion_set'))
    response = AgenciaTestCase.adjuntar_imagen_y_postear(c,'/admin/agencia/agenciado/add/',dict_form_agenciado)
    self.assertEqual(response.status_code,200)
    agenciado=Agenciado.objects.get(mail=u'testtrabajo01@gmail.com')
    self.assertIsInstance(agenciado,Agenciado)

