Instalación
-----------

* En settings.py agregar a INSTALLED\_APPS 'iampacks.cross.idioma'
* Defina en settigns.py la variable LANGUAGES con los idiomas que desea ofrecer.
* No olvide de agregar en su urls.py principal lo siguiente:

    url(r'^i18n/', include('django.conf.urls.i18n')),


Uso
---

* Para incluir una entrada de menú al estilo bootstrap puede reslizar lo siguiente en su template base:

    <ul class="nav">
      ...
      {% include 'idioma/language_menu.html' %}
      ...
    </ul>
    ...
    {% include 'idioma/language_form.html' %}

  EL language\_form.html debería incluirlo en al gún lugar antes de cerrar el tag body.
