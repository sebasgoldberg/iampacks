Iamsoft Packages
================

Installation
------------

Ubuntu 14 (Pillow prerequisites):

```
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

Install the package from git:

    $ pip install git+https://github.com/sebasgoldberg/iampacks.git

settings.py
-----------

Add into the bottom of the file:

```
from iampacks.agencia import agencia_set_settings, agencia_set_lang

LANGUAGES = []
agencia_set_lang(LANGUAGES)
agencia_set_settings(INSTALLED_APPS)
SITE_ID=1
```

if not is configured STATIC_ROOT, then configure as, for example:

```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

And create the folder 'static' in the django project directory.

urls.py
-------

Add the following to the urls.py project file:

```
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
```

Commands to be executed:
------------------------

```
./manage.py migrate
./manage.py collectstatic
./manage.py loadperfil
```