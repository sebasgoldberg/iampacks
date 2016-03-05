# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.models import User
from iampacks.agencia.notificacion.models import NotificacionCuentaAgenciadoExistente, MailInvalido
import imaplib
import re

RE_MAIL_INVALIDO = [
  '[ \n\r]*'.join('action not taken: mailbox unavailable'.split(' ')),
  '[ \n\r]*'.join('Host or domain name not found'.split(' ')),
  '[ \n\r]*'.join('The email account that you tried to reach does not exist'.split(' ')),
  '[ \n\r]*'.join('User unknown'.split(' ')),
  '[ \n\r]*'.join('Recipient address rejected'.split(' ')),
  '[ \n\r]*'.join("delivery error: dd This user doesn't have".split(' ')),
  '[ \n\r]*'.join('501 Invalid Address'.split(' ')),
  '[ \n\r]*'.join('Name service error for name'.split(' ')),
  '[ \n\r]*'.join('This account has been disabled or discontinued'.split(' ')),
  '[ \n\r]*'.join('said: 550 (in reply to RCPT TO command)'.split(' ')),
  '[ \n\r]*'.join('The email account that you tried to reach is over quota'.split(' ')),
  '[ \n\r]*'.join('Mailbox disabled for this recipient'.split(' ')),
  '[ \n\r]*'.join('Relay access denied'.split(' ')),
  '[ \n\r]*'.join('550 #5.1.0 Address rejected'.split(' ')),
  ]

RE_DIRECCION_MAIL_INVALIDO = re.compile('%s\r\nTo: ([^ ]+@[^ \r\n]+)'%settings.AMBIENTE.email.user)

class MailNoInvalido(Exception):
  pass

class DireccionEmailNoEncontrada(Exception):
  pass

class Command(BaseCommand):

  help=_(u'Detecta mails invalidos a partir de respuestas automáticas de servidores de mail.')

  option_list = BaseCommand.option_list + (
    make_option('--silencioso',default=False),
    )

  def get_mail_invalido(self, data):

    es_invalido = False

    for regexp in RE_MAIL_INVALIDO:
      if re.search(regexp,data):
        es_invalido = True
        break

    if not es_invalido:
      raise MailNoInvalido()

    match = re.search(RE_DIRECCION_MAIL_INVALIDO,data)

    if match:
      return match.group(1)

    if not self.silencioso:
      print data
      raise DireccionEmailNoEncontrada()

  def handle(self,*args,**options):

    self.silencioso = options['silencioso']

    imap = imaplib.IMAP4('localhost')
    imap.login(settings.AMBIENTE.email.user,settings.AMBIENTE.email.password)
    imap.select('inbox')
    
    result, data = imap.uid('search', None, 'ALL')

    uids = data[0].split(' ')

    for uid in uids:
      self.stdout.write('Se procesa el mensaje %s.\t'%uid)
      result, data = imap.uid('fetch', uid, '(RFC822)')

      try:
        email = self.get_mail_invalido(data[0][1])
        if email is not None:
          mail_invalido = MailInvalido.objects.get_or_create(email=email)
          imap.uid('STORE', uid, '+FLAGS', '(\\Deleted)')
      except MailNoInvalido:
        pass

    imap.expunge()
    imap.close()
    imap.logout()

