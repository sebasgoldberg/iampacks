from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from iampacks.agencia.trabajo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'alternativa.views.home', name='home'),
    # url(r'^alternativa/', include('alternativa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', 'index'),
    url(r'^agregar/agenciados/seleccionados/a/rol/$', views.agregar_agenciados_seleccionados_a_rol),
    url(r'^resultados/agregar/agenciados/seleccionados/a/rol/(\d+)/(.*)/$', views.resultados_agregar_agenciados_seleccionados_a_rol),
    url(r'^trabajo/enviar/mail/productora/(\d+)/$', views.trabajo_enviar_mail_productora),
    url(r'^trabajo/enviar/mail/agenciados/(\d+)/$', views.trabajo_enviar_mail_agenciados),
    url(r'^busquedas/$', views.busquedas),
    url(r'^portfolio/$', views.portfolio),
]
