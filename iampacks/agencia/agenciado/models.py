# coding=utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from iampacks.agencia.agencia.models import Agenciado
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.db.utils import IntegrityError
from django.conf import settings

def crear_usuario_agenciado(agenciado):
  if agenciado.user is None:
    if agenciado.mail is not None:
      nombre = agenciado.nombre
      apellido = agenciado.apellido
      username = '%s_%s_%s' % (nombre.replace(' ','')[:11],apellido.replace(' ','')[:11],str(agenciado.recurso_id))
      password = User.objects.make_random_password()
      agenciado.user = User.objects.create_user(username,agenciado.mail,password)
      agenciado.user.first_name = agenciado.nombre[:30]
      agenciado.user.last_name = agenciado.apellido[:30]
      agenciado.user.email = agenciado.mail 
      agenciado.user.save()
      agenciado.save()

# @todo Ver si va a aplicar lo de la creación automática del usuario por agenciado
@receiver(post_save, sender=Agenciado)
def callback_creacion_agenciado(sender, instance, created, raw, using, **kwargs):
  """
  Si se ha actualizado en el agenciado, el nombre apellido o email, se mantiene sincronizado con el usuario.
  """
  if instance.user is not None:
    modificado = False
    if instance.nombre[:30] != instance.user.first_name:
      instance.user.first_name = instance.nombre[:30]
      modificado = True
    if instance.apellido[:30] != instance.user.last_name:
      instance.user.last_name = instance.apellido[:30]
      modificado = True
    if instance.user.email != '' and instance.mail != instance.user.email:
      instance.user.email = instance.mail 
      modificado = True
    if modificado:
      instance.user.save()

@receiver(post_save, sender=User)
def callback_mail_creacion_usuario(sender, instance, created, raw, using, **kwargs):
  """
  Si se ha actualizado en el usuario, el nombre apellido o email, se mantiene sincronizado con el agenciado.
  """
  if created:
    return

  try:
    instance.agenciado
  except Agenciado.DoesNotExist:
    return

  modificado = False
  if instance.agenciado.nombre[:30] != instance.first_name:
    instance.agenciado.nombre = instance.first_name
    modificado = True
  if instance.agenciado.apellido[:30] != instance.last_name:
    instance.agenciado.apellido = instance.last_name
    modificado = True
  if instance.email != '' and instance.email != instance.agenciado.mail:
    instance.agenciado.mail = instance.email
    modificado = True
  if modificado:
    instance.agenciado.save()


