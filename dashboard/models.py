# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

PAISES = [('Colombia', 'Colombia'), ('Argentina', 'Argentina'), ('España', 'España'), ('Brasil', 'Brasil'),
          ('Venezuela', 'Venezuela'), ('Ecuador', 'Ecuador')]


class Ciudad (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    pais = models.CharField(max_length=20, choices=PAISES)
    departamento = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)


class Cliente (models.Model):
    identificacion = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M','M'), ('F','F')])
    fecha_nacimiento = models.DateField()
    ciudad_nacimiento = models.ForeignKey(Ciudad)
    direccion = models.CharField(max_length=256)
    telefono = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __unicode__(self):
        return unicode(u'{0} {1} - {2}'.format(self.nombres, self.apellidos, self.identificacion))


class Categoria (models.Model):
    nombre = models.CharField(max_length=100, unique=True) # for example: HW, SW and SERV
    codigo = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return unicode(self.nombre)


class Producto (models.Model):
    codigo = models.CharField(max_length=256, primary_key=True)
    nombre = models.CharField(max_length=256, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __unicode__(self):
        return unicode(u'{0} {1} - {2}'.format(self.nombre, self.codigo, self.precio))


class Vendedor (models.Model):
    nombre_completo = models.CharField(max_length=256)
    identificacion = models.BigIntegerField(primary_key=True)
    fecha_ingreso = models.DateField()

    def __unicode__(self):
        return unicode(u'{0}'.format(self.nombre_completo))


class Cotizacion (models.Model):
    fecha_cotizacion = models.DateTimeField(auto_now_add=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    iva = models.DecimalField(max_digits=10, decimal_places=1)
    total_cotizacion = models.DecimalField(max_digits=15, decimal_places=2)
    vendedor = models.ForeignKey(Vendedor)
    cliente = models.ForeignKey(Cliente)
    medio_de_pago = models.CharField(max_length=50, choices=[(1,'Debito'), (2,'Credito'), (3,'Efectivo')])
    pagado = models.BooleanField()
    descuento = models.DecimalField(max_digits=2, decimal_places=1)

    def __unicode__(self):
        return unicode(u'{0} {1} - {2}'.format(self.cliente.identificacion, self.medio_de_pago, self.pagado))


class Area (models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cantidad_empleados = models.IntegerField()

    def __unicode__(self):
        return unicode(self.nombre)


class Presupuesto (models.Model):
    fecha_presupuesto = models.DateField()
    cantidad_asignada = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    vigencia = models.IntegerField()  # vigencia en meses
    area = models.ForeignKey(Area)

    def __unicode__(self):
        return unicode(u'{0} - Presupuesta asignado:{1} - Vigencia:{2}'.format(self.area, self.cantidad_asignada, self.vigencia))

