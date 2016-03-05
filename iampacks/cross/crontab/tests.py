"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from iampacks.cross.crontab.models import Crontab
import subprocess
import os


class CrontabTest(TestCase):

    def test_add_line(self):
      crontab = Crontab()
      linea = u'linea de prueba'
      crontab.add_line(linea)
      comando = ['sudo', 'grep', linea, crontab.get_crontab()]
      with open(os.devnull,'w') as fnull:
        self.assertEqual(0,subprocess.call(comando, stdout=fnull))

      crontab.remove_line(linea)

    def test_remove_line(self):
      crontab = Crontab()
      linea = u'linea de prueba'
      not_erased_line = 'linea no borrada'

      crontab.add_line(linea)

      comando = ['sudo', 'grep', linea, crontab.get_crontab()]
      with open(os.devnull,'w') as fnull:
        self.assertEqual(0,subprocess.call(comando, stdout=fnull))

      crontab.add_line(not_erased_line)

      comando = ['sudo', 'grep', not_erased_line, crontab.get_crontab()]
      with open(os.devnull,'w') as fnull:
        self.assertEqual(0,subprocess.call(comando, stdout=fnull))

      crontab.remove_line(linea)

      comando = ['sudo', 'grep', linea, crontab.get_crontab()]
      with open(os.devnull,'w') as fnull:
        self.assertNotEqual(0,subprocess.call(comando, stdout=fnull))

      """
      Is verified that was not erased the line that has not to be deleted.
      """
      comando = ['sudo', 'grep', not_erased_line, crontab.get_crontab()]
      with open(os.devnull,'w') as fnull:
        self.assertEqual(0,subprocess.call(comando, stdout=fnull))

      crontab.remove_line(not_erased_line)
