from django.contrib import admin
from iampacks.agencia.notificacion.models import NotificacionCuentaAgenciadoExistente, MailInvalido

class NotificacionCuentaAgenciadoExistenteAdmin(admin.ModelAdmin):
  list_display=['id', 'agenciado', 'email_destinatario', 'fecha_envio']
  list_display_links = ('id', )
  date_hierarchy='fecha_envio'
  search_fields=['email_destinatario']

class MailInvalidoAdmin(admin.ModelAdmin):
  list_display=['id', 'email', 'fecha_deteccion', 'links_agenciados']
  list_display_links = ('id', )
  date_hierarchy='fecha_deteccion'
  search_fields=['email']

admin.site.register(NotificacionCuentaAgenciadoExistente, NotificacionCuentaAgenciadoExistenteAdmin)
admin.site.register(MailInvalido, MailInvalidoAdmin)
