"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from iampacks.cross.zonomi.models import Zonomi
import subprocess
from iampacks.cross.zonomi import settings as zonomi_settings

class ZonomiTest(TestCase):

    def test_add_domain_update_to_crontab(self):
        if zonomi_settings.ZONOMI_API_KEY is None:
            return
        zonomi = Zonomi()
        dominio = 'dominio.de.prueba'
        user = 'cerebro'
        zonomi.add_domain_update_to_crontab(dominio,user)
        self.assertEqual(0,subprocess.call(['grep', dominio, zonomi.get_crontab(user)]))
