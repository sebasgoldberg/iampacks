from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import subprocess
from django.template import loader
from django.template import Context
import logging
import traceback

class Command(BaseCommand):

  help=u'Crea la configuracion apache.'

  def __callScript(self,args,shell=False):
    return subprocess.check_output(args,shell=shell)

  def get_id(self):
    return settings.AMBIENTE.site_id

  def get_dominio(self):
    return settings.AMBIENTE.dominio

  def get_apache_site(self):
    return '%s.conf'%settings.AMBIENTE.site_id

  def get_apache_ssl_site(self):
    return '%s-ssl.conf' % settings.AMBIENTE.site_id

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

    self.__callScript(
      'echo -e "\\n\\n\\n\\n\\n\\n\\n" | sudo openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:2048 -keyout "%s" -out "%s"' % (
        self.get_certificate_file_name(),
        self.get_certificate_file_name(),
        ),
      shell=True)

  def create_apache2_conf(self):

    apache2_sites_available_path = '/etc/apache2/sites-available'

    template = loader.get_template('install/apache/conf')
    context = Context({
      'ID': self.get_id(),
      'DOMINIO': self.get_dominio(),
      'WD': settings.AMBIENTE.project_directory,
      'PUERTO_HTTP': settings.AMBIENTE.puerto_http,
      'PUERTO_HTTPS': settings.AMBIENTE.puerto_https,
      'MEDIA_ROOT': settings.MEDIA_ROOT,
      'STATIC_ROOT': settings.STATIC_ROOT,
      'WSGI_DIR': settings.AMBIENTE.wsgi_dir
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

    template = loader.get_template('install/apache/ssl-conf')
    context = Context({
      'ID': self.get_id(),
      'DOMINIO': self.get_dominio(),
      'WD': settings.AMBIENTE.project_directory,
      'PUERTO_HTTP': settings.AMBIENTE.puerto_http,
      'PUERTO_HTTPS': settings.AMBIENTE.puerto_https,
      'CERTIFICATE_FILE': self.get_certificate_file_name(),
      'MEDIA_ROOT': settings.MEDIA_ROOT,
      'STATIC_ROOT': settings.STATIC_ROOT,
      'WSGI_DIR': settings.AMBIENTE.wsgi_dir
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

  def crear_servicio(self):

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

    self.__callScript([
      'sudo',
      'service',
      'apache2',
      'reload'
      ])

  def handle(self,*args,**options):

    self.crear_servicio()

    self.stdout.write('Configuracion y activacion finalizada.\n')

