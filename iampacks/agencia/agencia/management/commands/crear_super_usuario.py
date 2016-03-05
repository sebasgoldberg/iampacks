# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.models import User

class Command(BaseCommand):

  help=_(u'Crea un super usuario para el proyecto en cuestión')

  option_list = BaseCommand.option_list + (
    make_option('--username'),
    make_option('--first_name'),
    make_option('--last_name'),
    make_option('--email'),
    make_option('--password'),
    )

  def handle(self,*args,**options):

    #try:
    
    username=options['username']
    first_name=options['first_name']
    last_name=options['last_name']
    email=options['email']
    password=options['password']

    user=User(
      username=username,
      first_name=first_name,
      last_name=last_name,
      email=email,
      is_staff=True,
      is_active=True,
      is_superuser=True,
      password=password
    )

    user.save()

    self.stdout.write(u'Nuevo super usuario creado con id %s\n'%user.id)

    #except Exception as e:

      #logger = logging.getLogger(__name__)
      #logger.error('Excepción ocurrida al intentar crear agencia con id "%s": %s' % (id,e))
