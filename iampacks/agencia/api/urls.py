from django.conf.urls import url, include

from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ojos', OjosViewSet)

router.register(r'ojos', OjosViewSet)
router.register(r'pelo', PeloViewSet)
router.register(r'piel', PielViewSet)
router.register(r'estado_dientes', EstadoDientesViewSet)
router.register(r'talle', TalleViewSet)
router.register(r'deporte', DeporteViewSet)
router.register(r'danza', DanzaViewSet)
router.register(r'instrumento', InstrumentoViewSet)
router.register(r'idioma', IdiomaViewSet)

router.register(r'agenciados', AgenciadoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^ciudad/$', AutocompleteCiudades.as_view()),
    url(r'^auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]

