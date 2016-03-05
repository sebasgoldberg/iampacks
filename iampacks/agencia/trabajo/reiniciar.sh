#!/bin/bash
python -c "import alternativa.settings"
if [ $? -ne 0 ]
then
  echo "ERROR: Este script debe ejecutarse desde la ruta del proyecto."
  exit 1
fi


(echo "drop table if exists trabajo_itemportfolio; " 
echo "drop table if exists trabajo_postulacion; "
echo "drop table if exists trabajo_eventorol; "
echo "drop table if exists trabajo_rol; "
echo "drop table if exists trabajo_telefonoproductora; "
echo "drop table if exists trabajo_direccionproductora; "
echo "drop table if exists trabajo_eventotrabajo; "
echo "drop table if exists trabajo_trabajo;"
echo "drop table if exists trabajo_productora;" 
) | mysql agencia -u agencia -p"$(python -c 'from alternativa.ambiente import ambiente; print ambiente.db.password')"
if [ $? -ne 0 ]
then
  exit 1
fi

mkdir -p uploads/trabajo/portfolio
mkdir -p uploads/cache/trabajo/portfolio
mkdir -p uploads/trabajo/trabajo
mkdir -p uploads/cache/trabajo/trabajo
mkdir -p uploads/trabajo/productora
mkdir -p uploads/cache/trabajo/productora
chmod 777 -R uploads

python manage.py syncdb 
if [ $? -ne 0 ]
then
  exit 1
fi

PRODUCTIVO=$(python -c "from alternativa.ambiente import ambiente; print ambiente.productivo")

if [ $? -ne 0 ]
then
  exit 1
fi

if [ "$PRODUCTIVO" = "False" ]
then
  python manage.py loaddata trabajo/fixtures/test-data
fi

exit 0
