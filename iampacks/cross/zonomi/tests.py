"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from iampacks.cross.zonomi.models import Zonomi
import subprocess

class ZonomiTest(TestCase):

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_add_domain_update_to_crontab(self):
        zonomi = Zonomi()
        dominio = 'dominio.de.prueba'
        user = 'cerebro'
        zonomi.add_domain_update_to_crontab(dominio,user)
        self.assertEqual(0,subprocess.call(['grep', dominio, zonomi.get_crontab(user)]))
