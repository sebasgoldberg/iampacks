# coding=utf-8

from django.conf import settings

SITIO_EXTERNO_URL = getattr(settings, 'SITIO_EXTERNO_URL', None)
