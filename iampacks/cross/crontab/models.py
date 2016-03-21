from django.db import models
import subprocess
from iampacks.cross.crontab import settings as crontab_settings
import os

class Crontab:

  def __init__(self,user=None,crontab_dir=None):
    if user:
      self.__user = user
    else:
      from django.conf import settings
      self.__user = crontab_settings.CRONTAB_USER

    if crontab_dir:
      self.__crontabs_dir = crontab_dir
    else:
      from django.conf import settings
      self.__crontabs_dir = crontab_settings.CRONTAB_DIR
  
  def get_crontab(self):
    return '%s/%s'%(self.__crontabs_dir,self.__user)

  def add_line(self,line):
    if not os.path.isfile(self.get_crontab()):
      params = [
        'sudo',
        'touch',
        self.get_crontab(),
        ]
      subprocess.check_output(params)
    params = [
      'sudo',
      'sed',
      '-i',
      "$a%s"%line,
      self.get_crontab(),
      ]
    subprocess.check_output(params)

  def remove_line(self,line):

    escaped_line=line.replace('/','\/')
    
    subprocess.check_output([
      'sudo',
      'sed',
      '-i',
      '/%s/d'%(escaped_line),
      self.get_crontab(),
      ])
