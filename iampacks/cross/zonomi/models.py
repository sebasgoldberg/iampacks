from django.db import models
import subprocess

class Zonomi:

  def __init__(self,api_key=None):

    if api_key:
      self.__api_key = api_key
    else:
      from django.conf import settings
      self.__api_key = settings.AMBIENTE.zonomi.api_key

    self.__base_url_service='https://zonomi.com/app/dns/dyndns.jsp'
  
  def domain_update(self,domain):
    subprocess.check_output([
      'wget',
      '-O',
      '-',
      '%s?host=%s&api_key=%s'%(self.__base_url_service, domain, self.__api_key),
      ])

  def delete_domain(self,domain):
    subprocess.check_output([
      'wget',
      '-O',
      '-',
      '%s?action=DELETE&name=%s&type=A&api_key=%s'%(self.__base_url_service, domain,self.__api_key),
      ])

  def add_domain_update_to_crontab(self,domain,user,ddns_log_file='/dev/null'):
    line = "*/30 * * * * wget -O - '%s?host=%s&api_key=%s' >> %s"%(self.__base_url_service, domain, self.__api_key, ddns_log_file)
    from iampacks.cross.crontab.models import Crontab
    crontab = Crontab(user=user)
    crontab.add_line(line)

  def remove_domain_update_from_crontab(self,domain,user):
    line = '%s?host=%s&api_key=%s'%(self.__base_url_service, domain,self.__api_key)
    from iampacks.cross.crontab.models import Crontab
    crontab = Crontab(user=user)
    crontab.remove_line(line)
