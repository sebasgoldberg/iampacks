# coding=utf-8
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy


class Disponibilidad(models.Model):

  DIAS_SEMANA=(
    (1, _(u'Lunes')),
    (2, _(u'Martes')),
    (3, _(u'Miércoles')),
    (4, _(u'Jueves')),
    (5, _(u'Viernes')),
    (6, _(u'Sábado')),
    (7, _(u'Domingo')),
  )
  DICT_DIAS_SEMANA=dict(DIAS_SEMANA)

  dia_desde = models.IntegerField(max_length=2,choices=DIAS_SEMANA, verbose_name=ugettext_lazy(u'Día desde'))
  dia_hasta = models.IntegerField(max_length=2,choices=DIAS_SEMANA, verbose_name=ugettext_lazy(u'Día hasta'), null=False, blank=False)
  hora_desde = models.TimeField(verbose_name=ugettext_lazy(u'Hora desde'), null=True, blank=True)
  hora_hasta= models.TimeField(verbose_name=ugettext_lazy(u'Hora hasta'), null=True, blank=True)

  def clean(self):
    if self.hora_desde and self.hora_hasta:
      if self.hora_desde >= self.hora_hasta:
        raise ValidationError(_(u'La hora desde debe ser menor a la hora hasta.'))

  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u"Disponibilidad")
    verbose_name_plural = ugettext_lazy(u"Disponibilidades")
