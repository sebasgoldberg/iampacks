# Create your views here.
from cities_light.models import Region, City
from django.shortcuts import render

def valores_select_estado(request,pais_id):
  return render(request,'direccion/valores_select.html', { 'valores': Region.objects.filter(country__id=pais_id).order_by('name')})

def valores_select_ciudad(request,estado_id):
  return render(request,'direccion/valores_select.html', { 'valores': City.objects.filter(region__id=estado_id).order_by('name')})
