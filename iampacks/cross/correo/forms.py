# coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy

class MailForm(forms.Form):
  # @todo Agregar múltiples destinatarios.
  destinatarios=forms.CharField(widget=forms.Textarea, help_text=ugettext_lazy(u'Adicione os destinatarios separados por ",", ";" ou salto de linea'))
  # @todo Ver de alargar el input
  asunto=forms.CharField(widget=forms.TextInput(attrs={'class':'asunto_mail'}))

  cuerpo=forms.CharField(widget=forms.Textarea, help_text=ugettext_lazy(u'Cuerpo del mail'))

  def get_destinatarios(self):
    destinatarios_text = self.cleaned_data['destinatarios']
    destinatarios = []
    for destinatario in destinatarios_text.replace('\n',',').replace(';',',').replace('\r',',').split(','):
      if destinatario != '':
        destinatarios+=[destinatario]
    return destinatarios
