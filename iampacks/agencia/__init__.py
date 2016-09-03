#encoding=utf8

AGENCIA_APPS = [
    'django.contrib.sites',
    'imagekit',
    'captcha',
    #'modeltranslation',
    'crispy_forms',
    'cities_light',
    'captcha',
    'modeltranslation',
    'iampacks.cross.estatico',
    'iampacks.cross.direccion',
    'iampacks.cross.telefono',
    'iampacks.cross.correo',
    'iampacks.cross.usuario',
    'iampacks.cross.idioma',
    'iampacks.cross.disponibilidad',
    'iampacks.agencia.perfil',
    'iampacks.agencia.agencia',
    'iampacks.agencia.agenciado',
    'iampacks.agencia.trabajo',
    'iampacks.agencia.notificacion',
    'iampacks.cross.install',
    'iampacks.cross.backup',
    'iampacks.cross.utils',
]

def agencia_set_settings(INSTALLED_APPS):

    for app in AGENCIA_APPS:
        if not app in INSTALLED_APPS:
            INSTALLED_APPS.append(app)

gettext = lambda s: s

def agencia_set_lang(LANGUAGES):
    LANGUAGES.append(('pt-br', gettext('Portugues')))
    LANGUAGES.append(('es', gettext('Spanish')))
