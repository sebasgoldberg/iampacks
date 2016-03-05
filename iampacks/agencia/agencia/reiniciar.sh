#!/bin/bash
python -c "import alternativa.settings"
if [ $? -ne 0 ]
then
  echo "ERROR: Este script debe ejecutarse desde la ruta del proyecto."
  exit 1
fi


echo "drop database agencia; create database agencia;" | mysql agencia -u agencia -p"$(python -c 'from alternativa.ambiente import ambiente; print ambiente.db.password')"
if [ $? -ne 0 ]
then
  exit 1
fi

echo "Se evita la migración de datos"
exit 0

cantidad=5

[ $# -gt 0 ] && cantidad="$1"

# Se borran las fotos y los thumbnails
rm -f uploads/agenciados/fotos/*
rm -f uploads/cache/agenciados/fotos/*

echo -e 'no\n' | python manage.py syncdb 
if [ $? -ne 0 ]
then
  exit 1
fi

python manage.py migrar "--cantidad=${cantidad}"
if [ $? -ne 0 ]
then
  exit 1
fi

python manage.py migrar-fotos
if [ $? -ne 0 ]
then
  exit 1
fi

exit 0
