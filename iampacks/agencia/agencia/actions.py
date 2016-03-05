from django.utils.translation import ugettext_lazy
from django.http import HttpResponseRedirect
from django.contrib import admin


def enviar_mail(modeladmin, request, queryset):

  selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
  return HttpResponseRedirect("/agencia/admin/agenciado/enviar/mail/?ids=%s" %  ",".join(selected))

enviar_mail.short_description=ugettext_lazy(u'Enviar mail a agenciados seleccionados')


def activar(modeladmin, request, queryset):
  queryset.update(activo=True)

activar.short_description=ugettext_lazy(u'Activar agenciados seleccionados')

