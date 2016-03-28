from django.conf.urls import url

from django.contrib import admin
from iampacks.agencia.agencia import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'alternativa.views.home', name='home'),
    # url(r'^alternativa/', include('alternativa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.index),
    url(r'^contacto/$', views.contacto),
    url(r'^admin/agenciado/enviar/mail/$', views.enviar_mail),
]

