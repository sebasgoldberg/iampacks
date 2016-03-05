# coding=utf-8
# Create your views here.

from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django import forms
from iampacks.agencia.trabajo.models import Postulacion, Rol, Trabajo, ItemPortfolio
from iampacks.agencia.agencia.models import Agenciado, Agencia
from django.template import loader, Context
from iampacks.agencia.agencia.mail import MailAgencia
from iampacks.agencia.trabajo.forms import MailProductoraForm, MailAgenciadosForm
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

class SeleccionarYAgregarAgenciadosForm(forms.ModelForm):
  ids = forms.CharField(widget = forms.HiddenInput(), required = True)
  class Meta:
    model = Postulacion
    fields = ('rol', 'estado')

# Verifica que tenga permisos el usuario para agregar agenciados a un trabajo
@permission_required('trabajo.add_postulacion',raise_exception=True)
def agregar_agenciados_seleccionados_a_rol(request):

  # Se obtienen los agenciados asociados a los IDs
  if request.method == 'GET':
    ids = request.GET['ids']
  else:
    ids = request.POST['ids']
  listado_ids=ids.split(',')
  agenciados=Agenciado.objects.filter(id__in=listado_ids)

  # Se crea el formulario con el campo trabajo y el campo estado en funcion del modelo Postulación
  # En caso de ser un metodo POST:
  if request.method == 'POST':
    form = SeleccionarYAgregarAgenciadosForm(request.POST)
    # Se valida el formulario
    if form.is_valid():
      # Se obtienen el trabajo y el estado seleccionados
      rol = form.cleaned_data['rol']
      estado_id = form.cleaned_data['estado']
      postulaciones_ya_existentes=[]
      postulaciones_realizadas_con_exito=[]
      # Por cada agenciado:
      for agenciado in agenciados:
        try:
          # Si el agenciado ya se encuentra asignado al trabajo, se guarda en el listado de agenciados ya asignados
          postulacion = Postulacion.objects.get(agenciado=agenciado.id,rol=rol.id)
          postulaciones_ya_existentes+=[postulacion]
          continue
        except Postulacion.DoesNotExist:
          # Sino, se asigna el agenciado al trabajo como una Postulacion con el estado seleccionado en el formulario y se guarda el agenciado en el listado de agenciados asignado con éxito
          postulacion=Postulacion(agenciado=agenciado, rol=rol, estado=estado_id)
          postulacion.save()
          postulaciones_realizadas_con_exito+=[postulacion]

      # Se obtienen los IDs de las postulacion como un string de ids separadas por comas.
      ids_exito = str([ int(str(postulacion.id)) for postulacion in postulaciones_realizadas_con_exito ])[1:-1]
      ids_existentes = str([ int(str(postulacion.id)) for postulacion in postulaciones_ya_existentes ])[1:-1]

      # Se muestran los resultados de la operación
      return redirect('/trabajo/resultados/agregar/agenciados/seleccionados/a/rol/%s/%s/?ids_exito=%s&ids_existentes=%s' % (
        rol.id,
        estado_id,
        ids_exito, 
        ids_existentes,))

  # Sino
  else:
    form = SeleccionarYAgregarAgenciadosForm(initial={'ids': ids})

  return render(request,'trabajo/rol/agregar_agenciados_seleccionados.html',{'form':form, 'agenciados':agenciados})

@permission_required('trabajo.add_postulacion',raise_exception=True)
def resultados_agregar_agenciados_seleccionados_a_rol(request,id_rol,id_estado):

  ids_exito = request.GET['ids_exito'].strip()
  if ids_exito:
    listado_ids_exito = [ int(x) for x in ids_exito.split(',') ]
  else:
    listado_ids_exito = []

  ids_existentes = request.GET['ids_existentes'].strip()
  if ids_existentes:
    listado_ids_existentes = [ int(x) for x in ids_existentes.split(',') ]
  else:
    listado_ids_existentes = []

  postulaciones_realizadas_con_exito=Postulacion.objects.filter(id__in=listado_ids_exito)
  postulaciones_ya_existentes=Postulacion.objects.filter(id__in=listado_ids_existentes)
  rol = Rol.objects.get(pk=id_rol)

  return render(request,'trabajo/rol/resultados_agregar_agenciados_seleccionados.html',
    {'postulaciones_realizadas_con_exito': postulaciones_realizadas_con_exito, 
    'postulaciones_ya_existentes': postulaciones_ya_existentes, 
    'rol': rol, 
    'estado': Postulacion.DICT_ESTADO_POSTULACION[id_estado] })

@permission_required('trabajo.mail_productora',raise_exception=True)
def trabajo_enviar_mail_productora(request,trabajo_id):
  
  trabajo=Trabajo.objects.get(pk=trabajo_id)

  if request.method == 'POST':
    form = MailProductoraForm(request.POST)
    if form.is_valid():
      template = loader.get_template('trabajo/trabajo/cuerpo_mail_productora.html')
      context = RequestContext(request, {'trabajo':trabajo, })
      asunto = form.cleaned_data['asunto']
      destinatarios = form.get_destinatarios()
      agencia=Agencia.get_activa(request)
      ccs = [request.user.email,agencia.email]

      text_content = _(u'Este mensagem deve ser visualizado em formato HTML.')
      html_content = template.render(context)
      msg = MailAgencia(asunto, text_content, destinatarios,ccs=ccs)
      msg.set_html_body(html_content)
      msg.send()
      messages.success(request, _(u'Trabalho enviado com sucesso a os seguintes destinatarios y copias: %(destinatarios)s %(copias)s') % {'destinatarios':str(destinatarios),'copias':str(ccs)})
      return redirect('/admin/trabajo/trabajo/%s/'%trabajo_id)
  else:
    asunto = _(u'Detalhe de trabalho "%s"') % (trabajo.titulo,)
    form = MailProductoraForm(initial={'destinatarios':trabajo.productora.mail, 'asunto': asunto })

  return render(request,'trabajo/trabajo/enviar_mail_productora.html',{'form': form, 'trabajo': trabajo, })

@permission_required('trabajo.mail_agenciados',raise_exception=True)
def trabajo_enviar_mail_agenciados(request,trabajo_id):
  
  trabajo=Trabajo.objects.get(pk=trabajo_id)

  if request.method == 'POST':
    form = MailAgenciadosForm(trabajo.rol_set.all(),request.POST)
    if form.is_valid():
      template = loader.get_template('trabajo/rol/admin/cuerpo_mail_agenciado.html')
      for rol in trabajo.rol_set.all():
        asunto = form.cleaned_data['asunto']
        agencia=Agencia.get_activa(request)
        ccs = [request.user.email,agencia.email]
        postulaciones = form.cleaned_data[MailAgenciadosForm.get_rol_fieldname(rol)]

        text_content = _(u'Este mensagem deve ser visualizado em formato HTML.')
        for postulacion in postulaciones:
          if postulacion.agenciado.mail:
            context = RequestContext(request, {'postulacion':postulacion, })
            html_content = template.render(context)
            destinatarios = [postulacion.agenciado.mail] + [x.email for x in postulacion.agenciado.mailagenciado_set.all()]
            msg = MailAgencia(asunto, text_content, destinatarios,ccs=ccs)
            msg.set_html_body(html_content)
            msg.send()
          else:
            messages.error(request, _(u'Agenciado %s não tem um email definido.'%postulacion.agenciado))
      messages.success(request, _(u'Trabalho enviado com sucesso a os agenciados selecionados.'))
      return redirect('/admin/trabajo/trabajo/%s/'%trabajo_id)
  else:
    asunto = _(u'Detalhe da Postulação para Trabalho "%s"') % (trabajo.titulo,)
    form = MailAgenciadosForm(trabajo.rol_set.all(),initial={'asunto': asunto})

  return render(request,'trabajo/trabajo/admin/enviar_mail_agenciados.html',{'form': form, 'trabajo': trabajo, })

def busquedas(request):
  trabajos=Trabajo.objects.filter(publicado=True).order_by('-fecha_ingreso')
  trabajo = None
  id=request.GET.get('id')
  if id is not None:
    try:
      trabajo = trabajos.get(pk=id)
    except Trabajo.DoesNotExist:
      pass
  return render(request,'trabajo/trabajo/busquedas.html',{'trabajos': trabajos,'trabajo':trabajo })

def portfolio(request):
  items=ItemPortfolio.objects.order_by('-fecha')

  paginator = Paginator(items, 9)
      
  page = request.GET.get('page')

  if page is None:
    page = 1

  try:
    portfolio = paginator.page(page)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    portfolio = paginator.page(paginator.num_pages)
                                              
  return render(request,'trabajo/itemportfolio/portfolio.html',{'portfolio': portfolio,})

