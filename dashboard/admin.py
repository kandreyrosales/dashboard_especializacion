# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from dashboard.models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'precio', 'cantidad', 'categoria')


class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'medio_de_pago', 'fecha_cotizacion', 'total_cotizacion', 'pagado')


# Register your models here.
# admin.site.register(Ciudad)
# admin.site.register(Cliente)
# admin.site.register(Categoria)
# admin.site.register(Producto, ProductoAdmin)
# admin.site.register(Vendedor)
# admin.site.register(Cotizacion, CotizacionAdmin)
# admin.site.register(Area)
# admin.site.register(Presupuesto)
admin.site.register(Usuario)
admin.site.register(Sucursal)
admin.site.register(ListaElectoral)
admin.site.register(Candidato)
admin.site.register(Voto)