# coding=utf-8

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import inlineformset_factory
from iampacks.agencia.agencia.forms import DireccionAgenciadoFormRelated
from django import forms
from iampacks.agencia.agencia.models import Agenciado, DireccionAgenciado, Telefono, FotoAgenciado, VideoAgenciado, DisponibilidadTrabajoAgenciado, TrabajoVigenteAgenciado, TrabajoRealizadoAgenciado
from iampacks.agencia.agencia.models import validarDireccionIngresada, validarTelefonoIngresado, validarFotoIngresada

from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from iampacks.agencia.agenciado.widgets import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import TabHolder, Tab, InlineCheckboxes

class AgenciadoForm(ModelForm):
  next_page = forms.CharField(widget=forms.HiddenInput,required=False)

  def __init__(self, *args, **kwargs):
    super(AgenciadoForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      TabHolder(
        Tab(_(u'Dados persoais'),
          'mail',
          'nombre',
          'apellido',
          'fecha_nacimiento',
          HTML("""
      <script>
        $('#id_fecha_nacimiento').datepicker({format: 'yyyy-mm-dd'})
      </script>
          """)
          ),
        Tab(_(u'Dados administrativos'),
          'documento_rg',
          'documento_cpf',
          'responsable',
          'cuenta_bancaria',
          ),
        Tab(_(u'Habilidades'),
          InlineCheckboxes('deportes'),
          InlineCheckboxes('danzas'),
          InlineCheckboxes('instrumentos'),
          InlineCheckboxes('idiomas'),
          )
        ),
      ButtonHolder(
        Submit('submit', 'Submit', css_class='button white')
      )
    )
  
  class Meta:
    model = Agenciado
    exclude = ('activo', 'fecha_ingreso')
    widgets = {
      'deportes': BPCheckboxSelectMultiple,
      'danzas': BPCheckboxSelectMultiple,
      'instrumentos': BPCheckboxSelectMultiple,
      'idiomas': BPCheckboxSelectMultiple,
      }

  class Media:
    js = ('bootstrap/js/bootstrap-datepicker.js',)
    css = { 'screen': ('bootstrap/css/datepicker.css',),}

class AgenciadoDatosPersonalesForm(ModelForm):
  class Meta:
    model = Agenciado
    fields = (
      'mail',
      'nombre',
      'apellido',
      'fecha_nacimiento',
      'documento_rg',
      'documento_cpf',
      'responsable',
      'cuenta_bancaria',
      )
  class Media:
    js = ('bootstrap/js/bootstrap-datepicker.js',)
    css = { 'screen': ('bootstrap/css/datepicker.css',),}

class AgenciadoCaracteristicasForm(ModelForm):
  class Meta:
    model = Agenciado
    fields = (
      'sexo',
      'ojos',
      'pelo',
      'piel',
      'altura',
      'peso',
      'talle',
      'talle_ropa_camisa',
      'talle_ropa_pantalon',
      'calzado',
      'estado_dientes',
      )

class AgenciadoHabilidadesForm(ModelForm):
  class Meta:
    model = Agenciado
    fields = (
      'deportes',
      'danzas',
      'instrumentos',
      'idiomas',
      )
    widgets = {
      'deportes': BPCheckboxSelectMultiple,
      'danzas': BPCheckboxSelectMultiple,
      'instrumentos': BPCheckboxSelectMultiple,
      'idiomas': BPCheckboxSelectMultiple,
      }

class AgenciadoOtrosDatosForm(ModelForm):
  class Meta:
    model = Agenciado
    fields = (
      'indicador_maneja',
      'indicador_tiene_registro',
      'trabaja_como_extra',
      'como_nos_conocio',
      'observaciones',
      )

BaseDireccionFormSet = inlineformset_factory(Agenciado, DireccionAgenciado, extra=1, max_num=1, can_delete=False, form = DireccionAgenciadoFormRelated)
BaseTelefonoFormSet = inlineformset_factory(Agenciado, Telefono, extra=1, max_num=6)
BaseFotoAgenciadoFormSet = inlineformset_factory(Agenciado, FotoAgenciado, extra=1, max_num=6)
VideoAgenciadoFormSet = inlineformset_factory(Agenciado, VideoAgenciado, extra=1, max_num=6, exclude=['codigo_video'])

DisponibilidadTrabajoAgenciadoFormSet = inlineformset_factory(Agenciado, DisponibilidadTrabajoAgenciado, extra=1, max_num=10)
TrabajoVigenteAgenciadoFormSet = inlineformset_factory(Agenciado, TrabajoVigenteAgenciado, extra=1, max_num=10)
TrabajoRealizadoAgenciadoFormSet = inlineformset_factory(Agenciado, TrabajoRealizadoAgenciado, extra=1, max_num=10)

class DireccionFormSet(BaseDireccionFormSet):
  def clean(self):
    super(DireccionFormSet,self).clean()
    validarDireccionIngresada(self)

class TelefonoFormSet(BaseTelefonoFormSet):

  def clean(self):
    super(TelefonoFormSet,self).clean()
    validarTelefonoIngresado(self)

class FotoAgenciadoFormSet(BaseFotoAgenciadoFormSet):
  def clean(self):
    super(FotoAgenciadoFormSet,self).clean()
    validarFotoIngresada(self)

