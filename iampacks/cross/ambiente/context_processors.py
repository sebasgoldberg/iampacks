from django.conf import settings

def add_ambiente(request):
    """
    Devuelve los datos del ambiente
    """
    return {'ambiente': settings.AMBIENTE }
