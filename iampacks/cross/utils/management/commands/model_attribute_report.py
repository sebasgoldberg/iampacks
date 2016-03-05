# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group
from django.utils.translation import activate, get_language
from optparse import make_option
from django.utils.translation import ugettext
from django.conf import settings
from importlib import import_module

class Command(BaseCommand):

  help=u'Obtiene un reporte acerca de un determinado atributo de un modelo.'

  option_list = BaseCommand.option_list + (
    make_option('--modelo'),
    make_option('--atributo'),
    )

  def import_class(self, cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = import_module(cl[0:d])
    c=getattr(m, classname)
    return c

  def report(self,Class,attribute):

    report={}
    for instance in Class.objects.all():
      value=getattr(instance,attribute)
      if report.has_key(value):
        report[value]+=1
      else:
        report[value]=1

    
    self.stdout.write('Valor\t\t\tCantidad\n')
    for valor, cantidad in report.iteritems():
      self.stdout.write('%s\t\t\t%s\n' % (str(valor).decode('utf-8'), cantidad))

  def handle(self,*args,**options):
    class_name = args[0]
    attribute_name= args[1]

    Class = self.import_class(class_name)

    self.report(Class,attribute_name)

