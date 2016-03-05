function cargar_valores_select_dependiente(select_padre,id_select_dependiente,url)
{
  if (select_padre.value)
  {
    jQuery.get(url,function(data,status){
      jQuery('#'+id_select_dependiente).html(data);
      });
  }
};

function change_pais(select_pais)
{
  id_select_estado=select_pais.id.replace('pais','estado');
  jQuery('#'+id_select_estado).html('<option value="">---------</option>');
  id_select_ciudad=id_select_estado.replace('estado','ciudad');
  jQuery('#'+id_select_ciudad).html('<option value="">---------</option>');
  url = '/direccion/valores/select/estado/'+select_pais.value+'/';
  cargar_valores_select_dependiente(select_pais,id_select_estado,url);
};

function change_estado(select_estado)
{
  id_select_ciudad=select_estado.id.replace('estado','ciudad');
  jQuery('#'+id_select_ciudad).html('<option value="">---------</option>');
  url = '/direccion/valores/select/ciudad/'+select_estado.value+'/';
  cargar_valores_select_dependiente(select_estado,id_select_ciudad,url);
};

