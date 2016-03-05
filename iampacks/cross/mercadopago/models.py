# coding=utf-8
from django.db import models
import requests
import json
from django.conf import settings
import hashlib
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class MercadoPago(object):
  
  MIME_JSON = "application/json"
  MIME_FORM = "application/x-www-form-urlencoded"

  def __init__(self,client_id=settings.AMBIENTE.mercado_pago.client_id,client_secret=settings.AMBIENTE.mercado_pago.client_secret):
    self.client_id=client_id
    self.client_secret=client_secret

  def get_access_token(self):
    params={
      'grant_type': 'client_credentials',
      'client_id': self.client_id,
      'client_secret': self.client_secret
      }
    response=requests.post('https://api.mercadolibre.com/oauth/token',params)
    return response.json()['access_token']

  def crear_usuario_prueba(self,site_id='MLA'):
    data=json.dumps({"site_id":site_id})
    response=requests.post(
      'https://api.mercadolibre.com/users/test_user?access_token=%s'%self.get_access_token(),
      data=data,
      headers={'Content-type':self.MIME_JSON, 'Accept':self.MIME_JSON}
      ).json()
    return response

  def get_pago(self,id_pago):
    response=requests.get(
      'https://api.mercadolibre.com/collections/%s?access_token=%s'%(id_pago,self.get_access_token()),
      headers={'Accept':self.MIME_JSON}
      )
    return response.json()

  def get_pagos(self):
    response=requests.get(
      'https://api.mercadolibre.com/collections/search?access_token=%s'%self.get_access_token(),
      headers={'Accept':self.MIME_JSON}
      )
    return response.json()

  def search_pagos_by_external_reference(self,external_reference):
    response=requests.get(
      'https://api.mercadolibre.com/collections/search?access_token=%s&external_reference=%s'%(self.get_access_token(),external_reference),
      headers={'Accept':self.MIME_JSON}
      )
    return response.json()

  EXTERNAL_REFERENCE='external_reference'
  
  STATUS='status'
  APPROVED='approved'

  STATUS_DETAIL='status_detail'
  ACCREDITED='accredited'

  def search_pagos_approved_and_accredited_by_external_reference(self,external_reference):
    response=requests.get(
      'https://api.mercadolibre.com/collections/search?access_token=%s&external_reference=%s&status=%s&status_detail=%s'%(self.get_access_token(),external_reference,MercadoPago.APPROVED,MercadoPago.ACCREDITED),
      headers={'Accept':self.MIME_JSON}
      )
    return response.json()

  def get_pago_notificado(self,id_notificacion_pago):
    response=requests.get(
      'https://api.mercadolibre.com/collections/notifications/%s?access_token=%s'%(id_notificacion_pago,self.get_access_token()),
      headers={'Accept':self.MIME_JSON}
      )
    return response.json()
    
class Pago(models.Model):

  class Meta:
    abstract=True
    verbose_name = _(u"Pago")
    verbose_name_plural = _(u"Pagos")
   
  #<!-- Datos obligatorios del item -->
  item_title = models.CharField(max_length=200, verbose_name=_(u'Descripción'))
  item_quantity = models.IntegerField()

  PESO_ARGENTINO = 'ARS' 
  DOLAR_ESTADOUNIDENSE = 'USD' 
  REAL = 'BRL' 
  PESO_MEXICANO = 'MXN' 
  BOLIVAR_FUERTE= 'VEF' 
  
  MONEDAS=(
    (PESO_ARGENTINO, _(u'Peso argentino')),
    (DOLAR_ESTADOUNIDENSE, _(u'Dólar estadounidense')),
    (REAL, _(u'Real')),
    (PESO_MEXICANO, _(u'Peso Mexicano')),
    (BOLIVAR_FUERTE, _(u'Bolívar fuerte')),
  )

  DICT_MONEDAS=dict(MONEDAS)

  item_currency_id = models.CharField(max_length=3,verbose_name=_(u'Moneda'), choices=MONEDAS, default=PESO_ARGENTINO)
  item_unit_price = models.DecimalField(max_digits=10,decimal_places=3, verbose_name=_(u'Precio unitario'))

  def total(self):
    return self.item_quantity*self.item_unit_price

  def descripcion_moneda(self):
    return Pago.DICT_MONEDAS[self.item_currency_id]
  
  def client_id(self):
    return settings.AMBIENTE.mercado_pago.client_id

  def md5(self):
    md5String = settings.AMBIENTE.mercado_pago.client_id + settings.AMBIENTE.mercado_pago.client_secret + str(self.item_quantity) + self.item_currency_id + self.item_unit_price_as_str() + self.item_id() + self.external_reference();
    return hashlib.md5(md5String).hexdigest()

  def item_id(self):
    return str(self.id)

  def external_reference(self):
    return str(self.id)

  #<!-- Datos opcionales -->
  def payer_name(self):
    """
    Este dato es opcional, por eso se devuelve vacío.
    Igualmente se aconseja redefinirlo y devolver el nombre del 
    usuario que está realizando el pago.
    """
    return u''

  def payer_surname(self):
    """
    Este dato es opcional, por eso se devuelve vacío.
    Igualmente se aconseja redefinirlo y devolver el apellido del 
    usuario que está realizando el pago.
    """
    return u''

  def payer_email(self):
    """
    Este dato es opcional, por eso se devuelve vacío.
    Igualmente se aconseja redefinirlo y devolver el email del 
    usuario que está realizando el pago.
    """
    return u''

  def back_url_success(self):
    return u''

  def back_url_pending(self):
    return u''

  def item_unit_price_as_str(self):
    return str(self.item_unit_price)

  def approved_and_accredited(self):
    mp=MercadoPago()
    respuesta=mp.search_pagos_approved_and_accredited_by_external_reference(self.external_reference())
    return respuesta['paging']['total']>=1

  def form_id(self):
    """
    Devuelve el id a asignar al formulario de pago.
    """
    return u"mercadopago_form_%s"%self.id
