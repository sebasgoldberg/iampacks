from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
from .permissions import IsOwner, IsAgenciadoOwner

from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from iampacks.agencia.agencia.models import Agenciado
from django.http import Http404

from iampacks.agencia.perfil.models import Ojos

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    #page_size_query_param = 'page_size'
    #max_page_size = 10000

def get_model_view_set(ModelSerializerClass, *args, **kwargs):
    kwargs['permissions'] = kwargs.get('permissions', [])
    kwargs['pagination'] = kwargs.get('pagination', LargeResultsSetPagination)
    class ModelViewSet(viewsets.ModelViewSet):
        queryset = ModelSerializerClass.Meta.model.objects.all()
        serializer_class = ModelSerializerClass
        permission_classes = kwargs['permissions']
        pagination_class = kwargs['pagination']
    return ModelViewSet

OjosViewSet = get_model_view_set(OjosSerializer)
PeloViewSet = get_model_view_set(PeloSerializer)
PielViewSet = get_model_view_set(PielSerializer)
EstadoDientesViewSet = get_model_view_set(EstadoDientesSerializer)
TalleViewSet = get_model_view_set(TalleSerializer)
DeporteViewSet = get_model_view_set(DeporteSerializer)
DanzaViewSet = get_model_view_set(DanzaSerializer)
InstrumentoViewSet = get_model_view_set(InstrumentoSerializer)
IdiomaViewSet = get_model_view_set(IdiomaSerializer)

UserViewSet = get_model_view_set(UserSerializer, permissions=(permissions.IsAuthenticated, IsOwner), pagination=PageNumberPagination)

AgenciadoViewSet = get_model_view_set(AgenciadoSerializer, permissions = (permissions.IsAuthenticated, IsAgenciadoOwner), pagination=PageNumberPagination)

