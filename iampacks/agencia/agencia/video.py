from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

class Video(models.Model):
  video = models.URLField(unique=True, null=True, blank=True)

  """
  El siguiente atributo debe ser asignado de la siguiente forma:
  @receiver(pre_save, sender=<Clase heredera de Video>)
  def callback_pre_save_video(sender, instance, raw, using, **kwargs):
    instance.url_to_codigo_video()
  """
  codigo_video = models.CharField(max_length=30, unique=True, null=True, blank=True)

  def __unicode__(self):
    return self.video

  class Meta:
    abstract = True
    verbose_name = ugettext_lazy(u"Video")
    verbose_name_plural = ugettext_lazy(u"Videos")

  def get_youtube_iframe_url(self):
    return (u'https://www.youtube.com/embed/%s' % self.codigo_video)
  get_youtube_iframe_url.allow_tags = True

  def html_youtube_iframe(self):
    return '<iframe width="373" height="210" src="%s" frameborder="0" allowfullscreen></iframe>' % self.get_youtube_iframe_url()
  html_youtube_iframe.allow_tags = True 

  def html_small_youtube_iframe(self):
    return '<iframe width="186" height="105" src="%s" frameborder="0" allowfullscreen></iframe>' % self.get_youtube_iframe_url()
  html_small_youtube_iframe.allow_tags = True 

  def url_to_codigo_video(self):
    if self.video is None:
      return
    if re.search('^.*v=',self.video):
      self.codigo_video = re.sub('^.*v=','',self.video)
      self.codigo_video = re.sub('&.*$','',self.codigo_video)
    elif re.search('[^?]',self.video):
      self.codigo_video = re.sub('^.*/','',self.video)

