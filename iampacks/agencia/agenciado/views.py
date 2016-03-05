# coding=utf-8
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from iampacks.agencia.agencia.models import Agenciado, DireccionAgenciado, Telefono, FotoAgenciado, VideoAgenciado, DisponibilidadTrabajoAgenciado, TrabajoVigenteAgenciado, TrabajoRealizadoAgenciado
from datetime import date
from django.contrib import messages
from iampacks.agencia.trabajo.models import Postulacion, Rol
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.agencia.agenciado.forms import *

def get_agenciado(request):
  try:
    agenciado=Agenciado.objects.get(user__id=request.user.id)
  except Agenciado.DoesNotExist:
    agenciado=Agenciado(
      user=request.user,
      nombre = request.user.first_name,
      apellido = request.user.last_name,
      mail = request.user.email,
      fecha_ingreso = date.today(),
      activo=False,
    )

  return agenciado

def process_agenciado_form(request,template,default_next_page):
  
  agenciado = get_agenciado(request)

  if request.method == 'POST':
    form = AgenciadoForm(request.POST,instance=agenciado)
    direccionFormSet = DireccionFormSet(request.POST,request.FILES,instance=agenciado)
    telefonoFormSet=TelefonoFormSet(request.POST,request.FILES,instance=agenciado)
    fotoAgenciadoFormSet=FotoAgenciadoFormSet(request.POST,request.FILES,instance=agenciado)
    videoAgenciadoFormSet=VideoAgenciadoFormSet(request.POST,request.FILES,instance=agenciado)
    disponibilidadTrabajoAgenciadoFormSet=DisponibilidadTrabajoAgenciadoFormSet(request.POST,request.FILES,instance=agenciado)
    trabajoVigenteAgenciadoFormSet=TrabajoVigenteAgenciadoFormSet(request.POST,request.FILES,instance=agenciado)
    trabajoRealizadoAgenciadoFormSet=TrabajoRealizadoAgenciadoFormSet(request.POST,request.FILES,instance=agenciado)
    if form.is_valid() and direccionFormSet.is_valid() and telefonoFormSet.is_valid() and fotoAgenciadoFormSet.is_valid() and videoAgenciadoFormSet.is_valid() and disponibilidadTrabajoAgenciadoFormSet.is_valid() and trabajoVigenteAgenciadoFormSet.is_valid() and trabajoRealizadoAgenciadoFormSet.is_valid():
      form.save()
      direccionFormSet.save()
      telefonoFormSet.save()
      fotoAgenciadoFormSet.save()
      videoAgenciadoFormSet.save()
      disponibilidadTrabajoAgenciadoFormSet.save()
      trabajoVigenteAgenciadoFormSet.save()
      trabajoRealizadoAgenciadoFormSet.save()
      messages.success(request, _(u'Dados atualizados com sucesso'))
      next_page = form.cleaned_data['next_page']
      if not next_page:
        next_page = default_next_page
      return redirect(next_page)
  else:
    next_page = request.GET.get('next')
    form = AgenciadoForm(instance=agenciado,initial={'next_page':next_page})
    direccionFormSet = DireccionFormSet(instance=agenciado)
    telefonoFormSet=TelefonoFormSet(instance=agenciado)
    fotoAgenciadoFormSet=FotoAgenciadoFormSet(instance=agenciado)
    videoAgenciadoFormSet=VideoAgenciadoFormSet(instance=agenciado)
    disponibilidadTrabajoAgenciadoFormSet=DisponibilidadTrabajoAgenciadoFormSet(instance=agenciado)
    trabajoVigenteAgenciadoFormSet=TrabajoVigenteAgenciadoFormSet(instance=agenciado)
    trabajoRealizadoAgenciadoFormSet=TrabajoRealizadoAgenciadoFormSet(instance=agenciado)
  return render(request,template,{
    'form':form, 
    'direccionFormSet':direccionFormSet,
    'telefonoFormSet':telefonoFormSet,
    'fotoAgenciadoFormSet':fotoAgenciadoFormSet,
    'videoAgenciadoFormSet':videoAgenciadoFormSet,
    'disponibilidadTrabajoAgenciadoFormSet': disponibilidadTrabajoAgenciadoFormSet,
    'trabajoVigenteAgenciadoFormSet': trabajoVigenteAgenciadoFormSet,
    'trabajoRealizadoAgenciadoFormSet': trabajoRealizadoAgenciadoFormSet,
    })


@login_required
def index(request): 
  return process_agenciado_form(request,'agenciado/agenciado.html','/agenciado/')

@login_required
def postular(request):
  # Se obtiene el rol de la postulación
  rol_id = request.GET.get('rol_id')
  try:
    rol = Rol.objects.get(pk=rol_id,trabajo__publicado=True)
  except Rol.DoesNotExist:
    messages.error(request,_(u'O perfil do trabalho para o qual quer aplicar nao foi encontrado'))
    return redirect('/trabajo/busquedas/')
  # Se verifica que el usuario tenga cargado su perfil
  try:
    request.user.agenciado
  except Agenciado.DoesNotExist:
    messages.info(request,
      _(u'Para aplicar ao perfil %(rol)s do trabalho <a href=%(url)s>%(trabajo)s</a> tem que completar seus dados de Agenciado')%{
        'rol':rol.descripcion,'url':'/trabajo/busquedas/?id=%s'%rol.trabajo.id,'trabajo':rol.trabajo.titulo})
    return redirect('/agenciado/?next=%s'%request.get_full_path())
  # Se realiza la postulación
  try:
    postulacion=Postulacion.objects.get(agenciado=request.user.agenciado,rol=rol)
  except Postulacion.DoesNotExist:
    postulacion=Postulacion(agenciado=request.user.agenciado,rol=rol,estado='PA')
    postulacion.save()

  messages.success(request,_(u'Aplicação para o perfil "%s" realizada com sucesso.')%rol.descripcion)
  messages.info(request,_(u'A aplicação vai ser analizada por nosso equipe, muito obrigado por sua postulação.'))
  return redirect('/trabajo/busquedas/?id=%s'%rol.trabajo.id)

