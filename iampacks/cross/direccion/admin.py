# coding=utf-8
from django.contrib import admin
from iampacks.cross.direccion.models import Direccion, Ciudad
from django.contrib.admin import SimpleListFilter
from cities_light.models import Region, Country
from django.utils.translation import ugettext as _

class FieldDireccionModelListFilter(SimpleListFilter):
  """
  Dado el siguiente modelo:

    from iampacks.cross.direccion.models import Direccion
    class DireccionProductora(Direccion):
      productora = models.ForeignKey(Productora, verbose_name=ugettext_lazy(u'Produtora'))

  Supongamos que en el listado del modelo Productora queremos filtrar por país,
  region y ciudad, simplemente deberíamos realizar lo siguiente:
  
    from iampacks.cross.direccion.admin import CiudadDireccionModelListFilter
    class ProductoraAdmin(admin.ModelAdmin):
      list_filter = (CiudadDireccionProductoraListFilter,
        EstadoDireccionProductoraListFilter, CiudadDireccionProductoraListFilter)

  Donde XxxxxxDireccionProductoraListFilter hereda de XxxxxxDireccionModelListFilter
  y define los atributos direccion_model y fk_field_model. Un ejemplo para una
  de las clases herederas sería:

    class PaisDireccionProductoraListFilter(PaisDireccionModelListFilter):
      direccion_model = DireccionProductora
      fk_field_model = 'productora'

  De esta forma se mostrarán los filtros para país, región y ciudad con
  valores que estén contenidos en las instancias DireccionProductora
  y que se correspondan con las instancias listadas de Productora
  """
  
  """
  Clase que hereda de Dirección y modela las direcciones de 
  algún modelo en particular, en el ejemplo DireccionProductora:
    direccion_model = DireccionProductora
  """
  direccion_model = None
  
  """
  Campo que contiene la FK al modelo al cual hace la referencia la
  direccion. En el ejemplo es el campo productora de la clase 
  DireccionProductora:
    fk_field_model = 'productora'
  """
  fk_field_model = None

  """
  Campo por el cual se filtrará, en el caso de las ciudades será 
  ciudad:
    direccion_field = 'ciudad'
  """
  direccion_field = None

  """
  Modelo del campo por el cual se está filtrando, en el caso de
  ciudad será:
    field_model = City
  """
  field_model = None

  """
  A ser asignado en caso que algún heredero de esta clase redefina 
  el método lookups. Se pasa como **kwargs al método filter del
  queryset del cual se obtienen los valores del filtro.
  """
  filtros_adicionales_valores = {}

  def lookups(self, request, model_admin):
    """
    Devuelve las ciudades obtenidas para los objetos del 
    modelo que hereda de Direccion
    """
    valores = ()
    ids = ()
    kwargs=self.filtros_adicionales_valores
    for valor in self.direccion_model.objects.filter(**kwargs).values(self.direccion_field):
      id = valor[self.direccion_field]
      if id:
        if id not in ids:
          ids += (id,)
          instance = self.field_model.objects.get(pk=id)
          valores+=((str(instance.id),instance.name),)

    return valores

  def queryset(self, request, queryset):
    """
    Filtra los valores a partir del valor seleccionado
    """
    if not self.value():
      return queryset.all()

    kwargs = {self.direccion_field:self.value()}
    valores = self.direccion_model.objects.filter(**kwargs).values(self.fk_field_model)
    return queryset.filter(id__in=[ valor[self.fk_field_model] for valor in valores])

class PaisDireccionModelListFilter(FieldDireccionModelListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Pais')
  # Parameter for the filter that will be used in the URL query.
  parameter_name = 'direccion_pais'
  direccion_field = 'pais'
  field_model = Country

  def lookups(self, request, model_admin):
    """
    En caso que se haya seleccionado un país, se seleccionarán los estados
    para dicho país. Sino no se mostrará el filtro.
    """
    estado_id = request.GET.get('direccion_estado')
    if estado_id:
      return None
    return super(PaisDireccionModelListFilter,self).lookups(request,model_admin)

class EstadoDireccionModelListFilter(FieldDireccionModelListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Estado')
  # Parameter for the filter that will be used in the URL query.
  parameter_name = 'direccion_estado'
  direccion_field = 'estado'
  field_model = Region

  def lookups(self, request, model_admin):
    """
    En caso que se haya seleccionado un país, se seleccionarán los estados
    para dicho país. Sino no se mostrará el filtro.
    """
    ciudad_id = request.GET.get('direccion_ciudad')
    if ciudad_id:
      return None
    pais_id = request.GET.get('direccion_pais')
    if pais_id:
      self.filtros_adicionales_valores={'pais__id':pais_id}
      return super(EstadoDireccionModelListFilter,self).lookups(request,model_admin)
    return None

class CiudadDireccionModelListFilter(FieldDireccionModelListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Cidade')
  # Parameter for the filter that will be used in the URL query.
  parameter_name = 'direccion_ciudad'
  direccion_field = 'ciudad'
  field_model = Ciudad

  def lookups(self, request, model_admin):
    """
    En caso que se haya seleccionado un estado, se seleccionarán las ciudades
    para dicho estado. Sino no se mostrará el filtro.
    """
    estado_id = request.GET.get('direccion_estado')
    if estado_id:
      self.filtros_adicionales_valores={'estado__id':estado_id}
      return super(CiudadDireccionModelListFilter,self).lookups(request,model_admin)
    return None


class BaseDireccionInline(admin.StackedInline):
  fieldsets=[
    (None, { 
      'fields':[ ('ciudad', ), ('barrio', 'direccion',), ('codigo_postal',)]}),
    ]
  raw_id_fields = ('ciudad',)
  autocomplete_lookup_fields = {
    'fk': ['ciudad'],
    }

admin.site.register(Ciudad)
