# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
import MySQLdb
from alternativa.ambiente import ambiente
import re
from iampacks.agencia.trabajo.models import ItemPortfolio
from datetime import date
import urllib
from django.core.files.images import ImageFile
import os

ID=0
TIPO=1
CODIGO=2
FECHA=3
TITULO=4

class Command(BaseCommand):

  help=u'Migrar el portfolio desde locaweb'
  

  def delete_portfolio(self):
    
    portfolio=ItemPortfolio.objects.all()

    for item in portfolio:
      item.delete()

  def handle(self,*args,**options):
    
    locaweb = ambiente.locaweb.db

    self.delete_portfolio()

    db = MySQLdb.connect(
      host=ambiente.locaweb.db.host,
      user=ambiente.locaweb.db.user,
      passwd=ambiente.locaweb.db.password,
      db=ambiente.locaweb.db.name)

    cur = db.cursor() 

    cur.execute("SELECT * FROM portifolio")
    fecha_mas_reciente = date(2008,5,1)

    for row in cur.fetchall():
      if row[FECHA] is None:
        fecha = fecha_mas_reciente
      else:
        fecha = row[FECHA]
        if fecha > fecha_mas_reciente:
          fecha_mas_reciente = fecha
      if row[TIPO] == 'V':
        if re.search('^http',row[CODIGO]):
          video=row[CODIGO]
        else:
          video = 'http://www.youtube.com/watch?v=%s' % row[CODIGO]
        item = ItemPortfolio(
          titulo = row[TITULO],
          video = video,
          fecha = fecha)
        item.url_to_codigo_video()
        if len(ItemPortfolio.objects.filter(codigo_video=item.codigo_video))==0:
          item.save()
          self.stdout.write(u'Item "%s", con fecha %s migrado con exito\n'.decode('utf-8') % (item.titulo.decode('utf-8'),item.fecha))
      if row[TIPO] == 'F':
        item = ItemPortfolio(
          titulo = row[TITULO],
          fecha = fecha)
        item.save()

        url = 'http://agenciaalternativa.com/portifolio/%s' % row[CODIGO]
        filename = '%s.jpg'%item.id 
        urllib.urlretrieve(url,filename)

        f=open(filename,'rb')
        imageFile=ImageFile(f)


        item.imagen.save(filename,imageFile,save=True)

        self.stdout.write(u'Item "%s", con fecha %s migrado con exito\n'.decode('utf-8') % (item.titulo.decode('utf-8'),item.fecha))

        f.close()

        os.remove(filename)
