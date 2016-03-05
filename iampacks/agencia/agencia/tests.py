# coding=utf-8
from iampacks.agencia.agencia.models import Agenciado, FotoAgenciado, VideoAgenciado, Telefono
from iampacks.agencia.perfil.models import Danza, Deporte, EstadoDientes, Idioma, Instrumento, Ojos, Pelo, Piel, Talle
from django.test import TestCase
from datetime import date
from datetime import timedelta
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail

class AgenciaTestCase(TestCase):

  fixtures = ['agencia/fixtures/test-data.yaml']

  @staticmethod
  def get_dict_form_agenciado(mail=u'test@gmail.com',rg=u'123100',cpf=u'123100'):
    return {
      'mail' : mail,
      ## Datos personales
      'nombre' : u'Test',
      'apellido' : u'Test',
      'fecha_nacimiento' : date(1982,12,20),
      ## Datos Administrativos
      'documento_rg' : rg,
      'documento_cpf' : cpf,
      'responsable' : u'Responsable de Test',
      #cuenta_bancaria: 
      ## Datos de direccion
      'estado' : Estado.objects.get().id,
      'ciudad' : Ciudad.objects.get().id,
      'barrio' : u'Barrio de Test',
      'direccion' : u'Direccion de Test',
      'codigo_postal' : u'1234',
      ## Caracteristicas fisicas
      'sexo' : u'M',
      'ojos' : Ojos.objects.get().id ,
      'pelo' : Pelo.objects.get().id ,
      'piel' : Piel.objects.get().id ,
      'altura' : 181,
      'peso' : 82,
      'talle' : Talle.objects.get().id ,
      'talle_camisa' : u'38',
      'talle_pantalon' : u'36',
      'calzado' : u'44',
      'estado_dientes' : EstadoDientes.objects.get().id ,
      ## Habilidades
      #deportes:
      #danzas: 
      #instrumentos: 
      #idiomas: 
      'indicador_maneja' : True,
      'indicador_tiene_registro' : False,
      ## Otros datos
      'trabaja_como_extra' : False,
      'como_nos_conocio' : u'Por Internet',
      #observaciones: 
      ## Datos administrativos del sistema 
      #'fecha_ingreso' : date(2013,01,14),

      'telefono_set-TOTAL_FORMS': u'1',
      'telefono_set-INITIAL_FORMS': u'0',
      'telefono_set-MAX_NUM_FORMS': u'',
      'telefono_set-0-compania': Compania.objects.get().id,
      'telefono_set-0-telefono': '123456789',

      'fotoagenciado_set-TOTAL_FORMS': u'1',
      'fotoagenciado_set-INITIAL_FORMS': u'0',
      'fotoagenciado_set-MAX_NUM_FORMS': u'',

      'videoagenciado_set-TOTAL_FORMS': u'1',
      'videoagenciado_set-INITIAL_FORMS': u'0',
      'videoagenciado_set-MAX_NUM_FORMS': u'',

      }

  @staticmethod
  def adjuntar_imagen_y_postear(client,url,dict_form_agenciado,imagen='test-data/burns.jpg'):
    f=open(imagen)
    dict_form_agenciado['fotoagenciado_set-0-foto'] = f
    response = client.post(url, dict_form_agenciado, follow = True)
    f.close()
    return response

  def test_creacion_agenciado(self):

    """
    Login de usuario inexistente
    """
    # Se accede al home
    c = Client()
    response = c.get('/',follow=True)
    self.assertEqual(response.status_code,200)

    # Se accede a la seccion de agenciados y se verifica una redirección a la página de login
    response = c.get('/agenciado/',follow=True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('registration/login.html' in [t.name for t in response.templates])
    self.assertTrue('http://testserver/accounts/login/?next=/agenciado/' in 
      [redirect[0] for redirect in response.redirect_chain])

    # Se intenta realizar el login de un usuario inexistente y se verifica un login fallido
    response = c.post('/accounts/login/',{'username': 'test', 'password': 'test'})
    self.assertEqual(response.status_code,200)
    self.assertTrue('registration/login.html' in [t.name for t in response.templates])
    self.assertFalse('agenciado/agenciado.html' in [t.name for t in response.templates])

    """
    Registro de usuario
    """
    # Se accede a la página de registro.
    response = c.get('/usuario/registro/')
    self.assertEqual(response.status_code,200)
    self.assertTrue('usuario/registro.html' in [t.name for t in response.templates])

    # Se registra un nuevo usuario y se verifica se muestre el formulario de agenciado.
    response = c.post('/usuario/registro/', {'username': 'test', 'password1': 'test', 'password2': 'test', 'first_name': 'Test', 'last_name': 'Last', 'email': 'test@gmail.com'}, follow = True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' in [t.name for t in response.templates])
    user=User.objects.get(username='test')
    self.assertIsInstance(user,User)

    # Se realiza un logout del agenciado registrado y 
    response = c.get('/usuario/logout/',follow=True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agencia/index.html' in [t.name for t in response.templates])

  #def test_ingreso_agenciado(self):

    """
    Login de usuario existente
    """
    # Se accede a la seccion de agenciados y se verifica una redirección a la página de login
    c = Client()
    response = c.get('/agenciado/',follow=True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('registration/login.html' in [t.name for t in response.templates])
    self.assertTrue('http://testserver/accounts/login/?next=/agenciado/' in 
      [redirect[0] for redirect in response.redirect_chain])

    # Se intenta realizar el login de un usuario ahora existente y se verifica la redirección a la sección de agenciados
    response = c.post('/accounts/login/',{'username': 'test', 'password': 'test'}, follow = True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' in [t.name for t in response.templates])

  #def test_carga_datos_perfil(self):

    """
    Creación de agenciado
    """
    # Se realiza el login
    c = Client()
    self.assertTrue(c.login(username = 'test', password = 'test'))

    # Se accede a la sección del perfil de agenciado
    response = c.get('/agenciado/')
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' in [t.name for t in response.templates])

    dict_form_agenciado=AgenciaTestCase.get_dict_form_agenciado()

    # Se intenta salvar los datos y se verifica que hay un error referente a las fotos del agenciado
    response = c.post('/agenciado/', dict_form_agenciado)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' in [t.name for t in response.templates])
    self.assertRaises(Agenciado.DoesNotExist,Agenciado.objects.get,user__username = 'test')
    self.assertFalse(len(response.context['fotoAgenciadoFormSet'].non_form_errors())==0)

    # Se agrega la foto y se intenta actualizar el perfil.
    response = AgenciaTestCase.adjuntar_imagen_y_postear(c,'/agenciado/',dict_form_agenciado)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' in [t.name for t in response.templates])
    # Se verifica que no existen errores
    for field in response.context['form']:
      self.assertTrue(len(field.errors)==0)
      #if len(field.errors)!=0:
        #raise Exception('%s\n%s' % (field,field.errors))
    self.assertTrue(len(response.context['telefonoFormSet'].non_form_errors())==0)
    self.assertTrue(len(response.context['fotoAgenciadoFormSet'].non_form_errors())==0)
    self.assertTrue(len(response.context['videoAgenciadoFormSet'].non_form_errors())==0)
    # Se verifica que el usuario tiene asociado un perfil de agenciado inactivo.
    agenciado=Agenciado.objects.get(user__username = 'test')
    self.assertIsInstance(agenciado,Agenciado)
    self.assertFalse(agenciado.activo)

    """
    Reseteo de clave
    """
    c=Client()
    response = c.get('/usuario/reiniciar/clave/')
    self.assertEqual(response.status_code,200)
    self.assertTrue('usuario/reiniciar_clave.html' in [t.name for t in response.templates])

    response = c.post('/usuario/reiniciar/clave/',{'email': agenciado.mail}, follow = True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('usuario/reiniciar_clave.html' in [t.name for t in response.templates])
    self.assertTrue(response.context['messages'])
    self.assertTrue(len(mail.outbox)>0)

  #def test_validacion_mail_registro(self):
    """
    Intento de registro de usuario con email ya existente
    """
    c=Client()
    # Se accede a la página de registro.
    response = c.get('/usuario/registro/')
    self.assertEqual(response.status_code,200)
    self.assertTrue('usuario/registro.html' in [t.name for t in response.templates])

    # Se registra un nuevo usuario y se verifica se muestre el formulario de agenciado.
    response = c.post('/usuario/registro/', {'username': 'test2', 'password1': 'test', 'password2': 'test', 'first_name': 'Test', 'last_name': 'Last', 'email': 'test@gmail.com'}, follow = True)
    self.assertEqual(response.status_code,200)
    self.assertTrue('agenciado/agenciado.html' not in [t.name for t in response.templates])
    self.assertRaises(User.DoesNotExist,User.objects.get,username = 'test2')


    """
    @todo Implementar test
    Verificación sincronización al modificar agenciado con usuario.
    """
