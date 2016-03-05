from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback

class Command(BaseCommand):

  help=u'Instala la agencia y la deja lista para usar.'

  def __callScript(self,args,shell=False):
    return subprocess.check_output(args,shell=shell)

  def get_id(self):
    return settings.AMBIENTE.id_agencia  

  def get_system_user(self):
    return settings.AMBIENTE.system_user

  def get_dominio(self):
    return settings.AMBIENTE.dominio

  def get_apache_site(self):
    return settings.AMBIENTE.id_agencia

  def get_apache_ssl_site(self):
    return '%s-ssl' % settings.AMBIENTE.id_agencia

  def set_ddns_updater(self):

    if settings.AMBIENTE.zonomi.api_key:
      ddns = Zonomi(settings.AMBIENTE.zonomi.api_key)
      ddns.domain_update(self.get_dominio())
      ddns.add_domain_update_to_crontab(self.get_dominio(),self.get_system_user())

  def enable_apache2_site(self):

    self.__callScript([
      'sudo',
      'a2ensite',
      self.get_apache_site(),
      ])

    self.__callScript([
      'sudo',
      'a2ensite',
      self.get_apache_ssl_site(),
      ])

    self.__callScript([
      'sudo',
      'service',
      'apache2',
      'reload'
      ])

  def get_certificate_file_name(self):
    return '/etc/apache2/ssl/%s.crt' % self.get_id()

  def create_certificate(self):

    self.__callScript([
      'sudo',
      'make-ssl-cert',
      '/usr/share/ssl-cert/ssleay.cnf',
      self.get_certificate_file_name()
      ])

  def create_apache2_conf(self):

    apache2_sites_available_path = '/etc/apache2/sites-available'

    template = loader.get_template('agencia/install/apache2/conf')
    context = Context({
      'AGENCIA': self.get_id(),
      'DOMINIO': self.get_dominio(),
      'WD_AGENCIA': settings.AMBIENTE.project_directory,
      'PUERTO_HTTP': settings.AMBIENTE.puerto_http,
      'PUERTO_HTTPS': settings.AMBIENTE.puerto_https,
      })
    apache2_conf = template.render(context)
    tmp_conf_file_name = '/tmp/%s' % (self.get_apache_site())
    apache2_conf_file = open(tmp_conf_file_name,'w')
    apache2_conf_file.write(apache2_conf)
    apache2_conf_file.close()
    apache2_conf_file_name = '%s/%s' % (apache2_sites_available_path,self.get_apache_site())
    self.__callScript([
      'sudo',
      'mv',
      tmp_conf_file_name,
      apache2_conf_file_name
      ])

    template = loader.get_template('agencia/install/apache2/ssl-conf')
    context = Context({
      'AGENCIA': self.get_id(),
      'DOMINIO': self.get_dominio(),
      'WD_AGENCIA': settings.AMBIENTE.project_directory,
      'PUERTO_HTTP': settings.AMBIENTE.puerto_http,
      'PUERTO_HTTPS': settings.AMBIENTE.puerto_https,
      'CERTIFICATE_FILE': self.get_certificate_file_name(),
      })
    apache2_conf = template.render(context)
    tmp_conf_file_name = '/tmp/%s' % (self.get_apache_ssl_site())
    apache2_conf_file = open(tmp_conf_file_name,'w')
    apache2_conf_file.write(apache2_conf)
    apache2_conf_file.close()
    apache2_conf_file_name = '%s/%s' % (apache2_sites_available_path,self.get_apache_ssl_site())
    self.__callScript([
      'sudo',
      'mv',
      tmp_conf_file_name,
      apache2_conf_file_name
      ])


  def copiar_informacion_ciudades(self):

    db_name_ciudades = settings.AMBIENTE.ciudades.db.name

    import MySQLdb 
    from getpass import getpass
    
    mysql_root_password = getpass("Enter mysql root password: ")

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
      os.makedirs('%s/uploads/agenciados/fotos'%settings.AMBIENTE.project_directory)
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      os.makedirs('%s/uploads/cache/agenciados/fotos'%settings.AMBIENTE.project_directory)
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      os.makedirs('%s/uploads/agencias/logos'%settings.AMBIENTE.project_directory)
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      self.__callScript([
        'chmod', '777', '-R', 'uploads'
        ])
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      os.makedirs('collectedstatic')
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    from django.core.management import call_command

    try:
      call_command('syncdb')
      call_command('migrate')
      call_command('syncdb','--all') # Necesario para que se carguen los permisos
      call_command('collectstatic')
      call_command('compilemessages')
      call_command('loadperfil','--idioma=%s'%settings.LANGUAGE_CODE)
      call_command('loadgroups')
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      self.copiar_informacion_ciudades()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      self.create_certificate()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      self.create_apache2_conf()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

    try:
      self.enable_apache2_site()
    except Exception:
      self.stdout.write('%s\n'%traceback.format_exc())

  def handle(self,*args,**options):

    self.crear_servicio()

    self.stdout.write('Instalacion finalizada.\n')

