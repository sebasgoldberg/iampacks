import requests

class Geocoder:
  
  json=None

  def __init__(self, direccion, ciudad='CABA', pais='AR'):
    
    r=requests.get( 
      'https://maps.googleapis.com/maps/api/geocode/json?address=%(direccion)s,+%(ciudad)s,+%(pais)s&sensor=false' % {
        'direccion': direccion,
        'ciudad': ciudad,
        'pais': pais
        })

    if r.status_code != 200:
      raise Exception('Codigo de estado en respuesta %s distinto de 200.' % r.status_code)

    self.json=r.json()

  def direccion_completa(self):
    return self.json['results'][0]['formatted_address']

  def barrio(self):
    for addr_comp in self.json['results'][0]['address_components']:
      for type in addr_comp['types']:
        if type == 'neighborhood':
          return addr_comp['long_name']
    raise Exception('Barrio no encontrado.')
    
  def latitud(self):
    return self.json['results'][0]['geometry']['location']['lat']

  def longitud(self):
    return self.json['results'][0]['geometry']['location']['lng']
