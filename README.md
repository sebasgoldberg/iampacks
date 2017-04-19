Iamsoft Packages
================

Installation
------------

Ubuntu 14 (Pillow prerequisites):

```
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

In case of using postgresql database:

```
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
pip install psycopg2
sudo su postgreso
createuser iampacks -P --interactive
createdb iampacks
psql
GRANT ALL PRIVILEGES ON database iampacks TO iampacks;
ALTER ROLE iampacks SET client_encoding TO 'utf8';
ALTER ROLE iampacks SET default_transaction_isolation TO 'read committed';
ALTER ROLE iampacks SET timezone TO 'UTC';
```

Install the package from git:

    $ pip install git+https://github.com/sebasgoldberg/iampacks.git

settings.py
-----------

If you want a jet look and feel add 'jet' before 'django.contrib.admin' in de INSTALLED_APPS list.

'django.contrib.postgres' necesary for TrigramSimilarity in INSTALLED_APPS.


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

if not configured MEDIA_ROOT and MEDIA_URL, then configure as, for example:


```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
```

Context Processors: Add the following:

```
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'iampacks.agencia.agencia.context_processors.agencia',
                ...
```

If you want a random list of thumbnails url of pictures from your resources, add the following:

```
                'iampacks.agencia.agencia.context_processors.thumbnails_urls',
```

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
from django.conf import settings

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')), #OPTIONAL
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

And to serv media files:

```
from django.views.static import serve
...
url(r'^media/(?P<path>.*)$', serve, {
  'document_root': settings.MEDIA_ROOT,
  }),
```


Commands to be executed:
------------------------

```
./manage.py migrate
./manage.py collectstatic
./manage.py loadperfil
```

Steps to Migrate From Iamcast:
------------------------------

Migrate the database:
====================

From Iamcast:

```
./manage.py dumpdata --format json --indent 2 -e sessions > data.json
```

To Iampacks:

```
./manage.py loaddata -i data.json
```

It is possible to get some errors, so, you have to remove the entries from data.json that is causing the errors.

Migrate the media:
==================

From Iamcast:

```
tar cvf uploads.tar.gz uploads
```

To Iampacks:

```
tar xvf uploads.tar.gz
```
settings.py (specific):
-----------------------

- SITIO_EXTERNO_URL (string, default None): To work with external site (if is defined, then, resource register fnuctionality is only available).
- PHOTO_MANDATORY (boolean, default None): To determine if the resource photo is mandatory.

Working With Multiple Agencies
==============================

- The django site framework should be enable.
- The corresponding site for each agancy should be created and assigned to de Agency.
- Each site/agency must use independent django settings file (defined generally in the wsgi script file).

So, basically you should create a new site, create a new agency, define a new settings file, define a new wsgi script.

Postgresql
----------

psql iampacks # version >=9.5
CREATE EXTENSION pg_trgm;
