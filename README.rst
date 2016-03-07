Iamsoft Packages
================

Installation
------------

Ubuntu 14 (Pillow prerequisites):

    $ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

Install the package from git:

    $ pip install git+https://github.com/sebasgoldberg/iampacks.git

settings.py
-----------

Add into the bottom of the file:

    from iampacks.agencia import agencia_set_settings

    agencia_set_settings(INSTALLED_APPS)

    SITE_ID=1
