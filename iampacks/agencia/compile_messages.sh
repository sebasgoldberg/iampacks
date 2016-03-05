#!/bin/bash

WD="$(readlink -f "$(dirname "$0")")"

function compile_module_messages
{
  cd "$WD/$1"
  django-admin.py compilemessages
}

compile_module_messages agencia
compile_module_messages agenciado
compile_module_messages perfil
compile_module_messages trabajo

