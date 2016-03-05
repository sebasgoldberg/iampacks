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

if [ $# -eq 1 ]
then
  make_module_messages "$1"
else
  make_module_messages agencia
  make_module_messages agenciado
  make_module_messages perfil
  make_module_messages trabajo
fi
