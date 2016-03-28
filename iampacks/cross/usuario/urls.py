from django.conf.urls import url
from iampacks.cross.usuario.forms import UsuarioAuthenticationForm
from django.contrib.auth.views import login
from django.contrib import admin
from iampacks.cross.usuario import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'alternativa.views.home', name='home'),
    # url(r'^alternativa/', include('alternativa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^cambio/clave/$', views.cambio_clave),
    url(r'^reiniciar/clave/$', views.reiniciar_clave),
    url(r'^logout/$', views.logout_view),
    url(r'^registro/$', views.registro),
    url(r'^login/$', login , {'authentication_form':UsuarioAuthenticationForm}),
]
