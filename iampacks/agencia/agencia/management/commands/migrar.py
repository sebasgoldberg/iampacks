# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from iampacks.agencia.agencia.models import Agenciado, FotoAgenciado, VideoAgenciado, Compania, Telefono, validarTelefonoIngresado, validarFotoIngresada
from iampacks.agencia.perfil.models import Danza, Deporte, EstadoDientes, Idioma, Instrumento, Ojos, Pelo, Piel, Talle
import pymssql
from django.core.files.images import ImageFile
import re
from optparse import make_option
from django.conf import settings

class Command(BaseCommand):

  compania_nextel = Compania.objects.get(descripcion='Nextel')

  help=u'Migra los datos actuales en la base de datos de produccion de la aplicacion DELPHI a la base de datos de esta aplicacion'

  option_list = BaseCommand.option_list + (
    make_option('--cantidad', default=5),
    make_option('--recurso'),
    )

  def migrarTablasSimples(self,cursor,tabla,clase):

    cursor.execute('SELECT * FROM '+tabla)

    for row in cursor:
      instanciaClase=clase(descripcion=row['descripcion'].decode('unicode-escape'))
      instanciaClase.save()

    self.stdout.write('La tabla %s se a migrado correctamente al modelo %s\n'%(tabla,clase))

  def get_object(self, model, descripcion):
    if descripcion is None:
      return None
    return model.objects.get(descripcion=descripcion.decode('unicode-escape'))

  def migrarTablaManyOneMany(self,tablaIntermedia,tablaDescripcion,claseModelo,relatedManager,recursoId):
    
    cursor=self.connection.cursor()

    cursor.execute(
      'select td.descripcion descripcion '+
      'from '+tablaIntermedia+' ti inner join '+tablaDescripcion+'s td '+
      'on ti.'+tablaDescripcion+'_id = td.id '+
      'where recurso_id = '+str(recursoId)
    )

    for row in cursor:
      instancia=claseModelo.objects.get(descripcion=row['descripcion'].decode('unicode-escape'))
      relatedManager.add(instancia)

  def addTelefono(self,agenciado,telefono, compania=None):
    
    if telefono == '':
      return

    agenciado.telefono_set.create( telefono = telefono, compania = compania )
    
  def migrarAgenciados(self,cursor):

    if int(self.cantidad) > 0:
      select='select top %s '%self.cantidad
    else:
      select='select '

    query="\
      %s \
        ag.id, \
        nombre, \
        apellido, \
        fecha_nacimiento, \
        sexo, \
        pi.descripcion piel, \
        direccion, \
        codigo_postal, \
        barrio, \
        ci.descripcion ciudad, \
        es.descripcion estado, \
        telefono_particular, \
        tel_particular_alt_1, \
        tel_particular_alt_2, \
        telefono_movil, \
        telefono_movil_alternativo_1, \
        telefono_movil_alternativo_2, \
        nextel, \
        responsable, \
        documento_RG, \
        documento_CPF, \
        altura, \
        peso, \
        ta.descripcion talle, \
        pe.descripcion pelo, \
        oj.descripcion ojos, \
        calzado, \
        esdi.descripcion estado_dientes, \
        talle_pantalon, \
        talle_camisa, \
        mail, \
        cuenta_bancaria, \
        indicador_maneja, \
        indicador_tiene_registro, \
        fecha_ingreso, \
        trabaja_como_extra, \
        como_nos_conocio, \
        observaciones \
      FROM \
        recurso ag left join piel pi \
        on ag.piel_id = pi.id \
        left join ciudad ci \
        on ag.ciudad_id = ci.id \
        left join estado es \
        on ag.estado_id = es.id \
        left join talle ta \
        on ag.talle_id = ta.id \
        left join pelo pe \
        on ag.pelo_id = pe.id \
        left join ojos oj \
        on ag.ojos_id = oj.id \
        left join estado_dientes esdi \
        on ag.estado_dientes_id = esdi.id "%select
    
    if self.recurso is not None:
      query += 'where ag.id = %s '%self.recurso

    cursor.execute(query)

    idRecursos={}

    for row in cursor:
      #self.stdout.write(row['descripcion']+'\n')
      piel=self.get_object(Piel,row['piel'])
      ciudad=self.get_object(Ciudad,row['ciudad'])
      estado=self.get_object(Estado,row['estado'])
      talle=self.get_object(Talle,row['talle'])
      pelo=self.get_object(Pelo,row['pelo'])
      ojos=self.get_object(Ojos,row['ojos'])
      estadoDientes=self.get_object(EstadoDientes,row['estado_dientes'])

      if row['mail'].decode('unicode-escape')=='':
        mail = None
      else:
        mail = row['mail'].decode('unicode-escape')

      repat=re.compile("^0*$")
      if repat.search(row['documento_CPF']) is None:
        documento_cpf = row['documento_CPF']
      else:
        documento_cpf = None

      agenciado=Agenciado(
        mail = mail,
        # Datos personales
        nombre = row['nombre'].decode('unicode-escape'),
        apellido = row['apellido'].decode('unicode-escape'),
        fecha_nacimiento = row['fecha_nacimiento'],
        # Datos Administrativos
        documento_rg = row['documento_RG'],
        documento_cpf = documento_cpf,
        responsable = row['responsable'].decode('unicode-escape'),
        cuenta_bancaria = row['cuenta_bancaria'],
        indicador_tiene_registro = row['indicador_tiene_registro'],
        # Datos de direccion
        estado = estado,
        ciudad = ciudad,
        barrio = row['barrio'].decode('unicode-escape'),
        direccion = row['direccion'].decode('unicode-escape'),
        codigo_postal = row['codigo_postal'],
        # Datos de contacto
        #nextel = row['nextel'],
        # Caracteristicas fisicas
        #SEXO=(
         # ('M', 'Masculino'),
         # ('F', 'Femenino'),
        #)
        sexo = row['sexo'],
        ojos = ojos,
        pelo = pelo,
        piel = piel,
        altura = row['altura'],
        peso = row['peso'],
        talle = talle,
        talle_camisa = row['talle_camisa'],
        talle_pantalon = row['talle_pantalon'],
        calzado = row['calzado'],
        estado_dientes = estadoDientes,
        # Habilidades
        #deportes = models.ManyToManyField(Deporte)
        #danzas = models.ManyToManyField(Danza)
        #instrumentos = models.ManyToManyField(Instrumento)
        #idiomas = models.ManyToManyField(Idioma)
        indicador_maneja = row['indicador_maneja'],
        # Otros datos
        trabaja_como_extra = row['trabaja_como_extra'],
        como_nos_conocio = row['como_nos_conocio'].decode('unicode-escape'),
        observaciones = row['observaciones'].decode('unicode-escape'),
        activo = True,
        fecha_ingreso = row['fecha_ingreso'],
        recurso_id = row['id']
        )

      agenciado.save()

      self.stdout.write('Agenciado %s creado con éxito a partir del recurso %s\n'%(agenciado.id,agenciado.recurso_id))
      
      idRecursos[agenciado.id]=row['id']
    
      self.addTelefono(agenciado,row['nextel'],self.compania_nextel)
      self.addTelefono(agenciado,row['telefono_particular'])
      self.addTelefono(agenciado,row['tel_particular_alt_1'])
      self.addTelefono(agenciado,row['tel_particular_alt_2'])
      self.addTelefono(agenciado,row['telefono_movil'])
      self.addTelefono(agenciado,row['telefono_movil_alternativo_1'])
      self.addTelefono(agenciado,row['telefono_movil_alternativo_2'])

    for idAgenciado, idRecurso in idRecursos.iteritems():

      agenciado=Agenciado.objects.get(id=idAgenciado)

      self.migrarTablaManyOneMany('Deporte_Recurso','Deporte',Deporte,agenciado.deportes,idRecurso)
      self.migrarTablaManyOneMany('Danza_Recurso','Danza',Danza,agenciado.danzas,idRecurso)
      self.migrarTablaManyOneMany('Instrumento_Recurso','Instrumento',Instrumento,agenciado.instrumentos,idRecurso)
      self.migrarTablaManyOneMany('Idioma_Recurso','Idioma',Idioma,agenciado.idiomas,idRecurso)

      self.stdout.write('Se migro correctamente el recurso %s en el agenciado %s\n'%(str(idRecurso),idAgenciado))

    self.stdout.write('La tabla %s se a migrado correctamente al modelo %s\n'%('recurso',Agenciado))


  def handle(self,*args,**options):

    self.cantidad=options['cantidad']
    self.recurso=options['recurso']

    self.connection = pymssql.connect(host=settings.AMBIENTE.mssqlserver.host, user='aretha', password='aretha01', database='alternativa', as_dict=True)
    cursor = self.connection.cursor()

    if self.recurso is None:
      self.migrarTablasSimples(cursor,'Ciudad',Ciudad)
      self.migrarTablasSimples(cursor,'Danzas',Danza)
      self.migrarTablasSimples(cursor,'Deportes',Deporte)
      self.migrarTablasSimples(cursor,'Estado',Estado)
      self.migrarTablasSimples(cursor,'Estado_Dientes',EstadoDientes)
      self.migrarTablasSimples(cursor,'Idiomas',Idioma)
      self.migrarTablasSimples(cursor,'Instrumentos',Instrumento)
      self.migrarTablasSimples(cursor,'Ojos',Ojos)
      self.migrarTablasSimples(cursor,'Pelo',Pelo)
      self.migrarTablasSimples(cursor,'Piel',Piel)
      self.migrarTablasSimples(cursor,'Talle',Talle)

    self.migrarAgenciados(cursor)

    self.connection.close()

