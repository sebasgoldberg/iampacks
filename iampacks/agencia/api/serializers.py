
from django.contrib.auth.models import User
from iampacks.agencia.agencia.models import *
from iampacks.agencia.perfil.models import *
from rest_framework import serializers

def get_serializer_class(Model, *arg, **kwargs):
    class NewClass(serializers.ModelSerializer):
        class Meta:
            model = Model
            fields = kwargs['fields']
    return NewClass

def get_basic_serializer_class(Model):
    return get_serializer_class(Model, fields=('id', 'descripcion'))

OjosSerializer = get_basic_serializer_class(Ojos)
PeloSerializer = get_basic_serializer_class(Pelo)
PielSerializer = get_basic_serializer_class(Piel)
EstadoDientesSerializer = get_basic_serializer_class(EstadoDientes)
TalleSerializer = get_basic_serializer_class(Talle)

DeporteSerializer = get_basic_serializer_class(Deporte)
DanzaSerializer = get_basic_serializer_class(Danza)
InstrumentoSerializer = get_basic_serializer_class(Instrumento)
IdiomaSerializer = get_basic_serializer_class(Idioma)

MailAgenciadoSerializer = get_serializer_class(MailAgenciado, fields=('id', 'email', 'descripcion'))
DireccionAgenciadoSerializer = get_serializer_class(DireccionAgenciado, fields=('id', 'descripcion', 'pais', 'estado', 'ciudad', 'barrio', 'direccion', 'codigo_postal',))
VideoAgenciadoSerializer = get_serializer_class(VideoAgenciado, fields=('id', 'video')) #@todo en iframe utilizar url de iframe
TelefonoSerializer = get_serializer_class(Telefono, fields=('id', 'telefono'))
DisponibilidadTrabajoAgenciadoSerializer = get_serializer_class(DisponibilidadTrabajoAgenciado, fields=('id', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta'))
TrabajoVigenteAgenciadoSerializer = get_serializer_class(TrabajoVigenteAgenciado, fields=('id', 'descripcion', 'fecha_vigencia'))
TrabajoRealizadoAgenciadoSerializer = get_serializer_class(TrabajoRealizadoAgenciado, fields=('id', 'descripcion', 'fecha_desde', 'fecha_hasta'))


class FotoAgenciadoSerializer(serializers.ModelSerializer):

    foto = serializers.ImageField()
    thumbnail = serializers.ImageField()
    mini_thumbnail = serializers.ImageField()

    class Meta:
        model = FotoAgenciado
        fields = ('id', 'foto', 'thumbnail', 'mini_thumbnail')

# Serializers define the API representation.
class AgenciadoSerializer(serializers.ModelSerializer):
    sexo = serializers.SerializerMethodField()

    #ojos = OjosSerializer(read_only=True)
    #pelo = PeloSerializer(read_only=True)
    #piel = PielSerializer(read_only=True)
    #estado_dientes = EstadoDientesSerializer(read_only=True)
    #talle = TalleSerializer(read_only=True)

    #deportes = DeporteSerializer(many=True, read_only=True)
    #danzas = DanzaSerializer(many=True, read_only=True)
    #instrumentos = InstrumentoSerializer(many=True, read_only=True)
    #idiomas = IdiomaSerializer(many=True, read_only=True)

    # Datos personales

    activo = serializers.BooleanField(read_only=True)
    fecha_ingreso = serializers.DateField(read_only=True)
    #site = serializers.ForeignKey(read_only=True)
 
    mailagenciado_set = MailAgenciadoSerializer(many=True, read_only=True)
    direccionagenciado_set = DireccionAgenciadoSerializer(many=True, read_only=True)
    fotoagenciado_set = FotoAgenciadoSerializer(many=True, read_only=True)
    videoagenciado_set = VideoAgenciadoSerializer(many=True, read_only=True)
    telefono_set = TelefonoSerializer(many=True, read_only=True)
    telefono_set = TelefonoSerializer(many=True, read_only=True)
    disponibilidadtrabajoagenciado_set = DisponibilidadTrabajoAgenciadoSerializer(many=True, read_only=True)
    trabajovigenteagenciado_set = TrabajoVigenteAgenciadoSerializer(many=True, read_only=True)
    trabajorealizadoagenciado_set = TrabajoRealizadoAgenciadoSerializer(many=True, read_only=True)

    class Meta:
        model = Agenciado
        fields = ( 'url',
            'mail', 'nombre', 'apellido', 'fecha_nacimiento', 'nombre_artistico', 
            'documento_rg', 'documento_cpf', 'documento_drt', 'responsable', 
            'cuenta_bancaria', 'sexo', 'ojos', 'pelo', 'piel', 'altura', 'peso', 
            'estado_dientes', 'talle', 'talle_camisa', 'talle_pantalon',
            'calzado', 'deportes', 'danzas', 'instrumentos', 
            'idiomas', 'indicador_maneja', 'indicador_tiene_registro', 'trabaja_como_extra', 
            'como_nos_conocio', 'observaciones', 'activo', 'fecha_ingreso', 'site',
            'mailagenciado_set', 'direccionagenciado_set', 'fotoagenciado_set',
            'videoagenciado_set', 'telefono_set', 'disponibilidadtrabajoagenciado_set',
            'trabajovigenteagenciado_set', 'trabajorealizadoagenciado_set',)

    def get_sexo(self, obj):
        return obj.get_sexo()

class UserSerializer(serializers.ModelSerializer):

    agenciado = AgenciadoSerializer()
    """
    agenciado = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='agenciado-detail'
    )
    """

    class Meta:
        model = User
        fields = ('agenciado', 'url', 'username', 'email', 'is_staff')


from iampacks.cross.direccion.models import Ciudad

class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = ('display_name', 'id')


