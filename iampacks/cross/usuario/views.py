# coding=utf-8
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import loader
from django.contrib import messages
from django.template import RequestContext
from iampacks.cross.usuario.forms import UsuarioSetPasswordForm, UsuarioPasswordResetForm, UserCreateForm
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from iampacks.cross.usuario.signals import usuario_after_register_before_redirect 
from django.conf import settings
from iampacks.cross.correo.mail import Mail

@login_required
def cambio_clave(request):
  if request.method == 'POST':
    form = UsuarioSetPasswordForm(request.user,request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, _(u'Sua senha foi trocada com sucesso'))
      return redirect('/usuario/cambio/clave/')
  else:
    form = UsuarioSetPasswordForm(request.user)


  return render(request,'usuario/cambio_clave.html',{'form':form})

def reiniciar_clave(request):
  if request.method == 'POST':
    form = UsuarioPasswordResetForm(request.POST)
    if form.is_valid():
      users=User.objects.filter(email=request.POST['email'])
      for user in users:
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()

        asunto = _(u'Sua senha ha mudado')
        template = loader.get_template('usuario/mail/cambio_clave.txt')
        context = RequestContext(request,{'usuario':user, 'clave':password})
        text_content = template.render(context)
        mail_class = get_mail_class()
        msg = mail_class(asunto,text_content,[user.email])
        msg.send()

        messages.success(request, _(u'Nova senha gerada com sucesso'))
        messages.info(request, _(u'Mail com nova senha enviado para %s')%user.email)

      next_page = form.cleaned_data['next_page']
      if not next_page:
        next_page = '/usuario/cambio/clave/'
      return redirect(next_page)
  else:
    form = UsuarioPasswordResetForm(initial={'next_page':request.GET.get('next')})

  return render(request,'usuario/reiniciar_clave.html',{'form':form,})

def logout_view(request):
  logout(request)
  return redirect('/')

from importlib import import_module

def import_class(cl):
  d = cl.rfind(".")
  classname = cl[d+1:len(cl)]
  m = import_module(cl[0:d])
  c=getattr(m, classname)
  return c

def get_mail_class():
  mail_class=Mail
  try:
    if settings.CORREO_CLASS:
      mail_class=import_class(settings.CORREO_CLASS)
  except AttributeError:
    pass
  return mail_class

def registro(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      user = form.save()
      user = authenticate(username=request.POST['username'], password=request.POST['password1'])
      login(request,user)

      asunto = _(u'Sua conta esta criada')
      template = loader.get_template('usuario/mail/creacion.txt')
      context = RequestContext(request)
      text_content = template.render(context)
      mail_class = get_mail_class()
      msg = mail_class(asunto, text_content, [user.email])
      msg.send()

      messages.success(request,_(u'Registro realizado com sucesso!'))
      messages.info(request,_(u'Enviamos para seu email dados da sua nova conta.'))
      usuario_after_register_before_redirect.send_robust(sender=user, request=request)

      next_page = form.cleaned_data['next_page']
      if not next_page:
        next_page = '/'

      return redirect(next_page)
  else:
    next_page = request.GET.get('next')
    form = UserCreateForm(initial={'next_page':next_page})

  return render(request,'usuario/registro.html',{'form':form, })
