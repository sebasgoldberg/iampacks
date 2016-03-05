# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group
from django.utils.translation import activate, get_language
from iampacks.agencia.perfil.models import *
from optparse import make_option
from django.utils.translation import ugettext
from django.conf import settings

class Command(BaseCommand):

  help=u'Carga datos de perfiles'

  option_list = BaseCommand.option_list + (
    make_option('--idioma'),
    )

  def load_entity(self,Class,descripcion):
    
    instance,created=Class.objects.get_or_create(descripcion=descripcion)
    current_language=get_language()
    self.stdout.write('%s.\n' % current_language)
    for (lang_code,_) in settings.LANGUAGES:
      activate(lang_code)
      instance.descripcion = ugettext(descripcion)
    activate(current_language)
    instance.save()

  def load_perfil_for_language(self):

    self.load_entity(Pelo,ugettext(u'Castanho'))
    self.load_entity(Pelo,ugettext(u'Castanho Claro'))
    self.load_entity(Pelo,ugettext(u'Grisalho'))
    self.load_entity(Pelo,ugettext(u'Loiro'))
    self.load_entity(Pelo,ugettext(u'Preto'))
    self.load_entity(Pelo,ugettext(u'Preto Claro'))
    self.load_entity(Pelo,ugettext(u'Ruiva'))

    self.load_entity(Danza,ugettext(u'Ballet'))
    self.load_entity(Danza,ugettext(u'Dança'))
    self.load_entity(Danza,ugettext(u'Dança de Rua'))
    self.load_entity(Danza,ugettext(u'Hip Hop'))
    self.load_entity(Danza,ugettext(u'Jazz'))
    self.load_entity(Danza,ugettext(u'Sapateado'))
    self.load_entity(Danza,ugettext(u'Street Dance'))
    self.load_entity(Danza,ugettext(u'Ventre'))
    self.load_entity(Danza,ugettext(u'Gafieira'))

    self.load_entity(Deporte,ugettext(u'Aeróbica'))
    self.load_entity(Deporte,ugettext(u'Anda a Cavalo'))
    self.load_entity(Deporte,ugettext(u'Atletismo'))
    self.load_entity(Deporte,ugettext(u'Ator'))
    self.load_entity(Deporte,ugettext(u'Basquete'))
    self.load_entity(Deporte,ugettext(u'Bicicleta'))
    self.load_entity(Deporte,ugettext(u'Boliche'))
    self.load_entity(Deporte,ugettext(u'Capoeira'))
    self.load_entity(Deporte,ugettext(u'Cavalgar'))
    self.load_entity(Deporte,ugettext(u'Ciclismo'))
    self.load_entity(Deporte,ugettext(u'Corrida c/ obstáculo'))
    self.load_entity(Deporte,ugettext(u'Futebol'))
    self.load_entity(Deporte,ugettext(u'Futsal'))
    self.load_entity(Deporte,ugettext(u'Ginastica Artistica'))
    self.load_entity(Deporte,ugettext(u'Ginastica Acrobática'))
    self.load_entity(Deporte,ugettext(u'Ginastica Olimpica'))
    self.load_entity(Deporte,ugettext(u'Ginastica Ritmica'))
    self.load_entity(Deporte,ugettext(u'Handeboll'))
    self.load_entity(Deporte,ugettext(u'Judo'))
    self.load_entity(Deporte,ugettext(u'Karate'))
    self.load_entity(Deporte,ugettext(u'Kung-fu'))
    self.load_entity(Deporte,ugettext(u'Locução'))
    self.load_entity(Deporte,ugettext(u'Maaythay'))
    self.load_entity(Deporte,ugettext(u'Natação'))
    self.load_entity(Deporte,ugettext(u'Patinação Artística'))
    self.load_entity(Deporte,ugettext(u'Patins'))
    self.load_entity(Deporte,ugettext(u'Power Jump'))
    self.load_entity(Deporte,ugettext(u'Rooler'))
    self.load_entity(Deporte,ugettext(u'samba'))
    self.load_entity(Deporte,ugettext(u'Skate'))
    self.load_entity(Deporte,ugettext(u'streetdance'))
    self.load_entity(Deporte,ugettext(u'Surf'))
    self.load_entity(Deporte,ugettext(u'Taekondo'))
    self.load_entity(Deporte,ugettext(u'Teatro'))
    self.load_entity(Deporte,ugettext(u'Tenis'))
    self.load_entity(Deporte,ugettext(u'Vôlei'))

    self.load_entity(EstadoDientes,ugettext(u'Bom'))
    self.load_entity(EstadoDientes,ugettext(u'Sem informação'))
    
    self.load_entity(Idioma,ugettext(u'Alemao'))
    self.load_entity(Idioma,ugettext(u'Chino'))
    self.load_entity(Idioma,ugettext(u'Espanhol'))
    self.load_entity(Idioma,ugettext(u'Francês'))
    self.load_entity(Idioma,ugettext(u'Inglês'))
    self.load_entity(Idioma,ugettext(u'Inglês intermediario'))
    self.load_entity(Idioma,ugettext(u'Italiano'))
    self.load_entity(Idioma,ugettext(u'Japones'))
    
    self.load_entity(Instrumento,ugettext(u'Acordeon'))
    self.load_entity(Instrumento,ugettext(u'Agogo'))
    self.load_entity(Instrumento,ugettext(u'Birimbal'))
    self.load_entity(Instrumento,ugettext(u'Canto'))
    self.load_entity(Instrumento,ugettext(u'Chocalho'))
    self.load_entity(Instrumento,ugettext(u'Escaleta'))
    self.load_entity(Instrumento,ugettext(u'Flauta'))
    self.load_entity(Instrumento,ugettext(u'Lira'))
    self.load_entity(Instrumento,ugettext(u'Orgão'))
    self.load_entity(Instrumento,ugettext(u'Pandeiro'))
    self.load_entity(Instrumento,ugettext(u'Percussão'))
    self.load_entity(Instrumento,ugettext(u'Piano'))
    self.load_entity(Instrumento,ugettext(u'Sino'))
    self.load_entity(Instrumento,ugettext(u'Tambor'))
    self.load_entity(Instrumento,ugettext(u'Teclado'))
    self.load_entity(Instrumento,ugettext(u'Timba'))
    self.load_entity(Instrumento,ugettext(u'Triângulo'))
    self.load_entity(Instrumento,ugettext(u'Trompete'))
    self.load_entity(Instrumento,ugettext(u'Violão'))
    self.load_entity(Instrumento,ugettext(u'Violino'))

    self.load_entity(Talle,ugettext(u'Robusta'))
    self.load_entity(Talle,ugettext(u'Gordo'))
    self.load_entity(Talle,ugettext(u'Magro'))
    self.load_entity(Talle,ugettext(u'Atletica'))
    self.load_entity(Talle,ugettext(u'Musculosa'))
    self.load_entity(Talle,ugettext(u'Normal'))

    self.load_entity(Ojos,ugettext(u'Azul'))
    self.load_entity(Ojos,ugettext(u'Castanho'))
    self.load_entity(Ojos,ugettext(u'Castanho Claro'))
    self.load_entity(Ojos,ugettext(u'Preto'))
    self.load_entity(Ojos,ugettext(u'Verdes'))

    self.load_entity(Piel,ugettext(u'Branca'))
    self.load_entity(Piel,ugettext(u'Morena'))
    self.load_entity(Piel,ugettext(u'Negra'))
    self.load_entity(Piel,ugettext(u'Oriental'))
    self.load_entity(Piel,ugettext(u'Parda'))

    self.load_entity(TalleRopa,ugettext(u'PP'))
    self.load_entity(TalleRopa,ugettext(u'P'))
    self.load_entity(TalleRopa,ugettext(u'M'))
    self.load_entity(TalleRopa,ugettext(u'G'))
    self.load_entity(TalleRopa,ugettext(u'GG'))

  def handle(self,*args,**options):

    self.load_perfil_for_language()

    self.stdout.write('Datos de perfiles cargados con exito.\n')


