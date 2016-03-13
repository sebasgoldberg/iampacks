# coding=utf-8

from django.conf import settings

EMAIL_USER = getattr(settings, 'EMAIL_USER', None)

