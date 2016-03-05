from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, UserCreationForm
from django import forms
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UsuarioAuthenticationForm(AuthenticationForm):

  def __init__(self, request=None, *args, **kwargs):

    self.helper = FormHelper()
    self.helper.form_class = 'uniForm'
    self.helper.form_method = 'post'
    self.helper.form_action = 'django.contrib.auth.views.login'
    self.helper.add_input(Submit('submit',_('Ingresar')))

    if request: 
      next_page = request.GET.get('next')
      if next_page:
        self.helper.add_input(Hidden('next', next_page))

    super(UsuarioAuthenticationForm, self).__init__(request, *args, **kwargs)

class UsuarioSetPasswordForm(SetPasswordForm):
  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_class = 'uniForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '/usuario/cambio/clave/'
    self.helper.add_input(Submit('submit',_('Trocar')))
    super(UsuarioSetPasswordForm, self).__init__(*args, **kwargs)

class UsuarioPasswordResetForm(PasswordResetForm):
  next_page = forms.CharField(widget=forms.HiddenInput,required=False)
  captcha = CaptchaField()
  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_class = 'uniForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '/usuario/reiniciar/clave/'
    self.helper.add_input(Submit('submit',_('Gerar')))
    super(UsuarioPasswordResetForm, self).__init__(*args, **kwargs)

def validate_unique_mail(value):
  users=User.objects.filter(email=value)
  if len(users)>0:
    raise ValidationError(_(u'O email ingresado ja existe'))

class UserCreateForm(UserCreationForm):
  next_page = forms.CharField(widget=forms.HiddenInput,required=False)
  captcha = CaptchaField()

  class Meta:
    model = User
    fields = ( "username", 'password1', 'password2', "email", "first_name", 'last_name', )

  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_class = 'uniForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '/usuario/registro/'
    self.helper.add_input(Submit('submit',_('Registrar')))
    super(UserCreateForm,self).__init__(*args, **kwargs)
    self.fields['email'].required=True
    self.fields['first_name'].required=True
    self.fields['last_name'].required=True
