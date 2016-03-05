
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback

class Command(BaseCommand):

  help=u'Asigna permisos escenciales.'

  def __callScript(self,args,shell=False):
    return subprocess.check_output(args,shell=shell)

  def crear_servicio(self):

    self.__callScript([
      'chmod',
      'g+rw',
      '-R',
      settings.MEDIA_ROOT
      ])

    self.__callScript([
      'sudo',
      'chgrp',
      'www-data',
      '-R',
      settings.MEDIA_ROOT
      ])

  def handle(self,*args,**options):

    self.crear_servicio()

    self.stdout.write('Configuracion y activacion finalizada.\n')

