from django.forms.widgets import Select
from django.forms import ModelForm, ModelChoiceField
from django.forms.util import ErrorList
from cities_light.models import Country, Region
from iampacks.cross.direccion.models import Ciudad
from iampacks.cross.direccion.models import COUNTRY_FILTER
from django.utils.translation import ugettext as _

class BaseDireccionForm(ModelForm):
  pass
 
class BaseDireccionFormRelated(ModelForm):
  def get_queryset(self,data,instance,prefix,campo,query_field,query_model):

    if prefix:
      nombre_campo = '%s-%s' % (prefix,campo)
    else:
      nombre_campo = campo

    if data and data[nombre_campo]:
      kwargs = {query_field+'__id':data[nombre_campo]}
    elif instance and getattr(instance,campo):
      kwargs = {query_field:getattr(instance,campo)}
    else:
      kwargs = {'id__in':[]}

    return query_model.objects.filter(**kwargs)

  def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, 
    initial=None, error_class=ErrorList, label_suffix=':',
    empty_permitted=False, instance=None):

    super(BaseDireccionFormRelated,self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)

    queryset_pais = Country.objects.filter(code2__in=COUNTRY_FILTER)
    queryset_region = self.get_queryset(data,instance,prefix,'pais','country',Region)
    queryset_ciudad = self.get_queryset(data,instance,prefix,'estado','region',Ciudad)

    self.fields['pais'] = ModelChoiceField(queryset=queryset_pais,widget=Select(attrs={'onchange':'change_pais(this)'}), label=_(u'Pais'))
    self.fields['estado'] = ModelChoiceField(queryset=queryset_region,widget=Select(attrs={'onchange':'change_estado(this)'}), label=_(u'Estado'))
    self.fields['ciudad'] = ModelChoiceField(queryset=queryset_ciudad, label=_(u'Cidade'))

  class Media:
    js = ('direccion/js/direccion.js',)
