# coding=utf-8

from django.conf import settings
import os

CRONTAB_USER = getattr(settings, 'CRONTAB_USER', os.getlogin())

# @todo make os dependant
CRONTAB_DIR = getattr(settings, 'CRONTAB_DIR', '/var/spool/cron/crontabs')

