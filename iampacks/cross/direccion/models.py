# coding=utf-8
from django.db import models
import cities_light
from cities_light.models import City, Region, Country
from django.utils.translation import ugettext_lazy
from django.db import router

COUNTRY_FILTER = ('AR', 'BR')

def filter_city_import(sender, items, **kwargs):
  if items[8] not in ('AR', 'BR'):
    raise cities_light.InvalidItems()

cities_light.signals.city_items_pre_import.connect(filter_city_import)

def filter_region_import(sender, items, **kwargs):
  if items[0].split('.')[0] not in ('AR', 'BR'):
    raise cities_light.InvalidItems()

cities_light.signals.region_items_pre_import.connect(filter_region_import)

class Ciudad(City):

  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)
 
  class Meta:
    proxy = True

class Direccion(models.Model):
  descripcion = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Descripção'),blank=True,null=True)
  pais = models.ForeignKey(Country,on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Pais'),null=True, blank=False, limit_choices_to = {'code2__in': COUNTRY_FILTER})
  estado = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Estado'),null=True, blank=False)
  ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, verbose_name=ugettext_lazy(u'Cidade'),null=True, blank=False)
  barrio = models.CharField(max_length=60, verbose_name=ugettext_lazy(u'Barrio'), blank=True, null=True)
  direccion = models.CharField(max_length=120, verbose_name=ugettext_lazy(u'Endereço'))
  codigo_postal = models.CharField(max_length=40, verbose_name=ugettext_lazy(u'CEP'), blank=True, null=True)

  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u"Endereço")
    verbose_name_plural = ugettext_lazy(u"Endereços")

  def __unicode__(self):
    return "%s, %s, %s, %s" % (self.direccion, self.barrio, self.ciudad, self.codigo_postal)

  def save(self, *args, **kwargs):
    if self.ciudad:
      self.estado = self.ciudad.region
    if self.estado:
      self.pais = self.estado.country
    super(Direccion, self).save(*args, **kwargs)
