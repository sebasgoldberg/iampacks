from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback

class Command(BaseCommand):

  help=u'Realiza un backup de la carpeta del proyecto y de la base de datos en el host configurado.'

  def __callScript(self,args,shell=False):
    return subprocess.check_output(args,shell=shell)

  def backup(self):

    self.__callScript(
      'mysqldump -u %(user)s -p%(password)s %(database)s > %(destination)s'% {
        'user': settings.AMBIENTE.db.user,
        'password': settings.AMBIENTE.db.password,
        'database': settings.AMBIENTE.db.name,
        'destination': '%s/mysql.backup'%settings.AMBIENTE.project_directory
      },shell=True)

    try:
      self.__callScript([
        'ssh',
        '%s@%s' % (
          settings.AMBIENTE.backup.user,
          settings.AMBIENTE.backup.host,
          ),
        'rm -rf %s' % settings.AMBIENTE.backup.destination,
        ])
    except:
      pass

    self.__callScript([
      'scp',
      '-r',
      settings.AMBIENTE.project_directory,
      '%s@%s:%s' % (
        settings.AMBIENTE.backup.user,
        settings.AMBIENTE.backup.host,
        settings.AMBIENTE.backup.destination,
        ),
      ])

  def handle(self,*args,**options):

    self.backup()

    self.stdout.write('Backup realizado con exito.\n')

