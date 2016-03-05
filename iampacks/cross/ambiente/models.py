# coding=utf-8

class BaseAmbiente:

  def get_base_url(self):
    return self.get_base_http()

  def get_base_http(self):
    if int(self.puerto_http) == 80:
      return 'http://%s' % self.dominio
    return 'http://%s:%s'%(self.dominio,self.puerto_http)

  def get_base_https(self):
    if int(self.puerto_https) == 443:
      return 'https://%s' % self.dominio
    return 'https://%s:%s'%(self.dominio,self.puerto_https)
