"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from iampacks.cross.usuario.forms import UsuarioAuthenticationForm
from django.views.generic import RedirectView
import iampacks
import django
import captcha

from iampacks.agencia.agencia import urls as agencia_urls
from iampacks.agencia.agenciado import urls as agenciado_urls
from django.contrib.auth.views import login
from captcha import urls as captcha_urls
from iampacks.agencia.trabajo import urls as trabajo_urls
from iampacks.cross.direccion import urls as direccion_urls
from iampacks.cross.usuario import urls as usuario_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agencia/', include(agencia_urls)),
    url(r'^agenciado/',include(agenciado_urls)),
    url(r'^accounts/login/$', login, {'authentication_form':UsuarioAuthenticationForm}),
    url(r'^captcha/', captcha_urls),
    url(r'^admin/password_reset/$', RedirectView.as_view(url='/usuario/reiniciar/clave/'), name='admin_password_reset'),
    #url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
      #{'document_root': settings.MEDIA_ROOT}),
    url(r'^trabajo/', trabajo_urls),
    url(r'^accounts/profile/$', iampacks.agencia.agenciado.views.index),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^direccion/',direccion_urls),
    url(r'^usuario/',usuario_urls),
    url(r'^$', RedirectView.as_view(url='/agencia/')),
]
