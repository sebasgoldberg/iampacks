#!/bin/bash

WD="$(readlink -f "$(dirname "$0")")"

function make_language_and_translate
{
  django-admin.py makemessages -l "$1"
  vim "locale/$1/LC_MESSAGES/django.po"
}

function make_module_messages
{
  cd "$WD/$1"
  echo "Creando mensajes para $1"
  make_language_and_translate "es"
  make_language_and_translate "pt_BR"
}

make_module_messages correo
make_module_messages crontab
make_module_messages direccion
make_module_messages estatico
make_module_messages idioma
make_module_messages mercadopago
make_module_messages telefono
make_module_messages usuario
make_module_messages zonomi
