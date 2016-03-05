import django.dispatch

usuario_after_register_before_redirect = django.dispatch.Signal(providing_args=['request'])
