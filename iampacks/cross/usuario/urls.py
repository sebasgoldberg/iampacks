from django.conf.urls import patterns, include, url
from django.conf import settings
from iampacks.cross.usuario.forms import UsuarioAuthenticationForm
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('iampacks.cross.usuario.views',
    # Examples:
    # url(r'^$', 'alternativa.views.home', name='home'),
    # url(r'^alternativa/', include('alternativa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^cambio/clave/$', 'cambio_clave'),
    url(r'^reiniciar/clave/$', 'reiniciar_clave'),
    url(r'^logout/$', 'logout_view'),
    url(r'^registro/$', 'registro'),
    url(r'^login/$', login , {'authentication_form':UsuarioAuthenticationForm}),
)

