# coding=utf-8
# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from iampacks.agencia.trabajo.models import Trabajo, ItemPortfolio
from iampacks.agencia.agencia.models import Agenciado, Agencia
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.cross.usuario.signals import usuario_after_register_before_redirect 
from django.conf import settings
from iampacks.agencia.agencia.forms import EnvioMailForm
from django.template import loader, Context
from django.template import RequestContext
from iampacks.agencia.agencia.mail import MailAgencia
from django.contrib import messages

def notify_register(sender,request,**kwargs):
  messages.info(request,_(u'Por favor atualize os dados do seu perfil a ser analizado por nossa agencia.'))

usuario_after_register_before_redirect.connect(notify_register)

def index(request):
  if settings.AMBIENTE.sitio.externo.url:
    return redirect(settings.AMBIENTE.sitio.externo.url)
  trabajos = Trabajo.objects.filter(publicado=True).order_by('-fecha_ingreso')[:3]
  portfolio = ItemPortfolio.objects.order_by('-fecha')[:3]
  return render(request,'agencia/index.html', { 'trabajos': trabajos, 'portfolio': portfolio})

def contacto(request):
  return render(request,'agencia/contacto.html')

@permission_required('agencia.edit_agenciado',raise_exception=True)
def enviar_mail(request):

  # Se crea el formulario con el campo trabajo y el campo estado en funcion del modelo Postulación
  # En caso de ser un metodo POST:
  if request.method == 'POST':
    form = EnvioMailForm(request.POST)
    # Se valida el formulario
    if form.is_valid():
      template = loader.get_template('correo/base.html')
      context = RequestContext(request, {'cuerpo':form.cleaned_data['cuerpo'], })
      asunto = form.cleaned_data['asunto']
      agencia=Agencia.get_activa(request)
      destinatarios = [agencia.email,]
      ccs = [request.user.email,]
      bccs = form.get_destinatarios()
      text_content = _(u'Este mensagem deve ser visualizado em formato HTML.')
      html_content = template.render(context)
      msg = MailAgencia(asunto, text_content, destinatarios,ccs=ccs,bccs=bccs)
      msg.set_html_body(html_content)
      msg.send()
      messages.success(request, _(u'Mails enviados con éxito'))

      return redirect('/admin/agencia/agenciado/')

  # Sino
  else:
    # Se obtienen los agenciados asociados a los IDs
    if request.method == 'GET':
      ids = request.GET['ids']
    else:
      ids = request.POST['ids']
    listado_ids=ids.split(',')
    agenciados=Agenciado.objects.filter(id__in=listado_ids)

    destinatarios = []
    for agenciado in agenciados:
      for mail in agenciado.get_mails():
        destinatarios.append(mail)
      
    form = EnvioMailForm(initial={'destinatarios': '\n'.join(destinatarios)})

  return render(request,'admin/agencia/agenciado/enviar_mail.html',{'form':form})

