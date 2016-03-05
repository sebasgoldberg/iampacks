Instalación
-----------

* Instalar iampacks.cross.correo
* Agregar en settings.INSTALLED\_APPS:

  'iampacks.cross.usuario',

* Agregar en <mi-proyecto>/urls.py:

  url(r'^usuario/', include('iampacks.cross.usuario.urls')),

* En caso que lo desee puede agregar un menu dropdown a su página principal (precisa bootstrap, JQuery y crispy\_forms):
  
  <ul class="nav">
    {% include 'usuario/dropdown_menu.html' with link_cuenta_usuario='</url/a/mi/cuenta/>' %}
  </ul>


