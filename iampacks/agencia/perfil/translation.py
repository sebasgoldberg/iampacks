from modeltranslation.translator import translator, TranslationOptions
from iampacks.agencia.perfil.models import *

class DanzaTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Danza, DanzaTranslationOptions)

class DeporteTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Deporte, DeporteTranslationOptions)

class EstadoDientesTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(EstadoDientes, EstadoDientesTranslationOptions)

class IdiomaTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Idioma, IdiomaTranslationOptions)

class InstrumentoTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Instrumento, InstrumentoTranslationOptions)

class OjosTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Ojos, OjosTranslationOptions)

class PeloTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Pelo, PeloTranslationOptions)

class PielTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Piel, PielTranslationOptions)

class TalleTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Talle, TalleTranslationOptions)

class TalleRopaTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(TalleRopa, TalleRopaTranslationOptions)

