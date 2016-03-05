#!/bin/bash

WD="$(readlink -f "$(dirname "$0")")"

function compile_module_messages
{
  cd "$WD/$1"
  django-admin.py compilemessages
}

compile_module_messages correo
compile_module_messages crontab
compile_module_messages direccion
compile_module_messages estatico
compile_module_messages idioma
compile_module_messages mercadopago
compile_module_messages telefono
compile_module_messages usuario
compile_module_messages zonomi
