# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
import pymssql

class Command(BaseCommand):

  help=u'Realiza una consulta a la base de datos de la aplicación DELPHI'
  args=u'<consulta-sql consulta-sql ...>'

  def consultar(self,consulta):
    
    self.stdout.write('Ejecucion de la consulta %s\n'%consulta)

    cursor=self.connection.cursor()

    cursor.execute(consulta)

    for row in cursor:
      for field in row:
        self.stdout.write('%s\t'%row[field])
      self.stdout.write('\n')

  def handle(self,*args,**options):

    self.connection = pymssql.connect(host='25.92.66.172', user='aretha', password='aretha01', database='alternativa', as_dict=True)

    for consulta in args:
      self.consultar(consulta)

    self.connection.close()


