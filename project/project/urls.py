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
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agencia/', include('iampacks.agencia.agencia.urls')),
    url(r'^agenciado/', include('iampacks.agencia.agenciado.urls')),
    url(r'^accounts/login/$', login, {'authentication_form':UsuarioAuthenticationForm}),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/password_reset/$', RedirectView.as_view(url='/usuario/reiniciar/clave/'), name='admin_password_reset'),
    url(r'^trabajo/',include('iampacks.agencia.trabajo.urls')),
    url(r'^accounts/profile/$', iampacks.agencia.agenciado.views.index),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^direccion/',include('iampacks.cross.direccion.urls')),
    url(r'^usuario/',include('iampacks.cross.usuario.urls')),
    url(r'^$', RedirectView.as_view(url='/agencia/')),
]
