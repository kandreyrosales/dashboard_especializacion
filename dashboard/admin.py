# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from dashboard.models import *

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Cotizacion)
admin.site.register(Area)
admin.site.register(Presupuesto)