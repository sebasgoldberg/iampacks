# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy

class Compania(models.Model):
  descripcion = models.CharField(max_length=100, unique=True, verbose_name=ugettext_lazy(u'Descripção'))
  def __unicode__(self):
    return self.descripcion
  class Meta:
    ordering = ['descripcion']

class Telefono(models.Model):
  compania = models.ForeignKey(Compania, null=True, blank=True,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Compania'))
  telefono = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Telefone'))
  def __unicode__(self):
    return ugettext_lazy(u'%(telefono)s (%(compania)s)') % {'telefono':self.telefono,'compania':self.compania}
  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(ugettext_lazy(u"Telefone"))
    verbose_name_plural = ugettext_lazy(u"Telefones")
