#encoding=utf8

AGENCIA_APPS = [
    'cities_light',
    'iampacks.cross.telefono',
    'iampacks.cross.direccion',
    'iampacks.agencia.perfil',
    'iampacks.agencia.agencia',
    'iampacks.agencia.agenciado',
    'iampacks.agencia.trabajo',
    'iampacks.agencia.notificacion',
]

def agencia_set_settings(INSTALLED_APPS):

    for app in AGENCIA_APPS:
        if not app in INSTALLED_APPS:
            INSTALLED_APPS.append(app)
