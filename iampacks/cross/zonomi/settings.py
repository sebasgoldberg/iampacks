# coding=utf-8

from django.conf import settings

ZONOMI_API_KEY = getattr(settings, 'ZONOMI_API_KEY', None)

