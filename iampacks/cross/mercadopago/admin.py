from django.contrib import admin

class PagoAdmin(admin.ModelAdmin):
  list_display=['id','item_title','item_id','external_reference','item_quantity','item_unit_price','item_currency_id']

