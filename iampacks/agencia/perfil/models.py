# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

class Danza(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Dança")
      verbose_name_plural = ugettext_lazy(u"Danças")

class Deporte(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Esporte")
      verbose_name_plural = ugettext_lazy(u"Esportes")

class EstadoDientes(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Estado Dentes")
      verbose_name_plural = ugettext_lazy(u"Estados Dentes")

class Idioma(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']

class Instrumento(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']

class Ojos(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Olhos")
      verbose_name_plural = ugettext_lazy(u"Olhos")

class Pelo(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Cabelo")
      verbose_name_plural = ugettext_lazy(u"Cabelos")

class Piel(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Pele")
      verbose_name_plural = ugettext_lazy(u"Peles")

class Talle(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Manequim")
      verbose_name_plural = ugettext_lazy(u"Manequims")

class TalleRopa(models.Model):
    descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripción'))
    def __unicode__(self):
      return self.descripcion
    class Meta:
      ordering = ['descripcion']
      verbose_name = ugettext_lazy(u"Talle Ropa")
      verbose_name_plural = ugettext_lazy(u"Talle Ropa")
