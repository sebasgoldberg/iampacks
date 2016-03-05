from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback
from iampacks.cross.install.management.commands.dbcreate import InstallCommand

class Command(InstallCommand):

  help=u'Carga los datos de ciudades.'

  def copiar_informacion_ciudades(self):

    db_name_ciudades = settings.AMBIENTE.ciudades.db.name

    import MySQLdb 
    from getpass import getpass
    
    mysql_root_password = self.get_mysql_root_password()

    mysql_connection = MySQLdb.connect(
      'localhost', 
      'root',
      mysql_root_password
      )

    cursor = mysql_connection.cursor()
    
    try:
      cursor.execute("insert into %s.cities_light_country select * from %s.cities_light_country"%(settings.AMBIENTE.db.name,db_name_ciudades))
      cursor.execute("insert into %s.cities_light_region select * from %s.cities_light_region"%(settings.AMBIENTE.db.name,db_name_ciudades))
      cursor.execute("insert into %s.cities_light_city select * from %s.cities_light_city"%(settings.AMBIENTE.db.name,db_name_ciudades))
      mysql_connection.commit()
    except:
      mysql_connection.rollback()

    mysql_connection.close()

  def crear_servicio(self):

    try:
      self.copiar_informacion_ciudades()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

  def handle(self,*args,**options):

    self.crear_servicio()

    self.stdout.write('Copia finalizada.\n')

