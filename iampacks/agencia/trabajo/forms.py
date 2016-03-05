# coding=utf-8
from iampacks.cross.correo.forms import MailForm
from django import forms
from django.utils.translation import ugettext_lazy
from django.forms import ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _

class MailProductoraForm(MailForm):
  def __init__(self, *args, **kwargs):
    super (MailProductoraForm, self).__init__(*args,**kwargs)
    self.fields.pop('cuerpo')

class MailAgenciadosForm(forms.Form):
  asunto=forms.CharField(widget=forms.TextInput(attrs={'class':'asunto_mail'}), help_text=_(u'Indique el asunto de los emails a ser enviados.'))

  @staticmethod
  def get_rol_fieldname(rol):
    return u'agenciados_rol_%s'%rol.id

  def __init__(self,queryset_roles,*args,**kwargs):
    super(MailAgenciadosForm,self).__init__(*args,**kwargs)
    for rol in queryset_roles:
      fieldname=MailAgenciadosForm.get_rol_fieldname(rol)
      if not fieldname in self.fields:
        self.fields[fieldname] = ModelMultipleChoiceField(queryset=rol.postulacion_set.all().order_by('estado'),label=rol,widget=CheckboxSelectMultiple, help_text=_(u'Indique los destinatarios del mail para el perfil "%s"') % rol, required=False)

from django.test import TestCase
class MailAgenciadosFormTestCase(TestCase):

  def test_crear_formulario(self):
    from iampacks.agencia.agencia.models import Agenciado
    form = MailAgenciadosForm('Postulado para casting',Agenciado.objects.all())
