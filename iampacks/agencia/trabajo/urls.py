from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('iampacks.agencia.trabajo.views',
    # Examples:
    # url(r'^$', 'alternativa.views.home', name='home'),
    # url(r'^alternativa/', include('alternativa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', 'index'),
    url(r'^agregar/agenciados/seleccionados/a/rol/$', 'agregar_agenciados_seleccionados_a_rol'),
    url(r'^resultados/agregar/agenciados/seleccionados/a/rol/(\d+)/(.*)/$', 'resultados_agregar_agenciados_seleccionados_a_rol'),
    url(r'^trabajo/enviar/mail/productora/(\d+)/$', 'trabajo_enviar_mail_productora'),
    url(r'^trabajo/enviar/mail/agenciados/(\d+)/$', 'trabajo_enviar_mail_agenciados'),
    url(r'^busquedas/$', 'busquedas'),
    url(r'^portfolio/$', 'portfolio'),
)

