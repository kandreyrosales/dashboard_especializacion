# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

PAISES = [('Colombia', 'Colombia')]

DEPARTAMENTOS = [('Cesar', 'Cesar'),
                 ('Atlántico', 'Atlántico'),
                 ('La Guajira', 'La Guajira'), ('Magdalena', 'Magdalena'),
                 ('Bolivar', 'Bolivar'), ('Córdoba', 'Córdoba')]


class Ciudad (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    pais = models.CharField(max_length=20, choices=PAISES)
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTOS)

    def __str__(self):
        return self.nombre


# class Cliente (models.Model):
#     identificacion = models.BigIntegerField(primary_key=True)
#     nombres = models.CharField(max_length=256)
#     apellidos = models.CharField(max_length=256)
#     sexo = models.CharField(max_length=1, choices=[('M', 'M'), ('F', 'F')])
#     fecha_nacimiento = models.DateField()
#     ciudad_nacimiento = models.ForeignKey(Ciudad)
#     direccion = models.CharField(max_length=256)
#     telefono = models.CharField(max_length=50)
#     email = models.EmailField()
#     activo = models.BooleanField(default=True)
#
#     def __str__(self):
#         return '{0} {1} - {2}'.format(self.nombres, self.apellidos, self.identificacion)
#
#
# class Categoria (models.Model):
#     nombre = models.CharField(max_length=100, unique=True) # for example: HW, SW and SERV
#     codigo = models.CharField(max_length=100, primary_key=True)
#
#     def __str__(self):
#         return self.nombre
#
#
# class Producto (models.Model):
#     codigo = models.CharField(max_length=256, primary_key=True)
#     nombre = models.CharField(max_length=256, unique=True)
#     precio = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
#     cantidad = models.IntegerField()
#     categoria = models.ForeignKey(Categoria)
#     costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
#
#     def __str__(self):
#         return '{0} {1} - {2}'.format(self.nombre, self.codigo, self.precio)
#
#
# class Vendedor (models.Model):
#     nombre_completo = models.CharField(max_length=256)
#     identificacion = models.BigIntegerField(primary_key=True)
#     fecha_ingreso = models.DateField()
#
#     def __str__(self):
#         return '{0}'.format(self.nombre_completo)
#
#
# class Cotizacion (models.Model):
#     fecha_cotizacion = models.DateTimeField(auto_now_add=True, blank=False)
#     precio = models.DecimalField(max_digits=10, decimal_places=3)
#     iva = models.DecimalField(max_digits=10, decimal_places=1)
#     total_cotizacion = models.DecimalField(max_digits=15, decimal_places=2)
#     vendedor = models.ForeignKey(Vendedor)
#     cliente = models.ForeignKey(Cliente)
#     medio_de_pago = models.CharField(max_length=50, choices=[('No aplica', 'No aplica'), ('Debito', 'Debito'),
#                                                              ('Credito', 'Credito'), ('Efectivo', 'Efectivo')])
#     pagado = models.CharField(max_length=2, choices=[('Si','Si'), ('No', 'No')])
#     descuento = models.DecimalField(max_digits=3, decimal_places=1)
#     productos = models.ManyToManyField(Producto)
#
#     def __str__(self):
#         return '{0} {1} - {2}'.format(self.cliente.identificacion, self.medio_de_pago, self.pagado)
#
#
# class Area (models.Model):
#     nombre = models.CharField(max_length=100, unique=True)
#     cantidad_empleados = models.IntegerField()
#
#     def __str__(self):
#         return self.nombre
#
#
# class Presupuesto (models.Model):
#     fecha_presupuesto = models.DateField()
#     cantidad_asignada = models.DecimalField(max_digits=15, decimal_places=3, blank=True)
#     vigencia = models.IntegerField()  # vigencia en meses
#     area = models.ForeignKey(Area)
#
#     def __str__(self):
#         return '{0} - Presupuesta asignado:{1} - Vigencia:{2}'.format(self.area, self.cantidad_asignada, self.vigencia)
#
####################################################
class Sucursal (models.Model):
    nombre = models.CharField(max_length=256, unique=True, null=False)
    codigo = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return self.nombre


class Candidato (models.Model):
    identificacion = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=256, verbose_name='Nombre Completo')
    genero = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    imagen = models.ImageField()
    fecha_nacimiento = models.DateField()
    sucursal = models.ForeignKey(Sucursal)

    def __str__(self):
        return '{0} {1} {2}'.format(self.nombre, self.identificacion, self.sucursal)


class ListaElectoral (models.Model):
    numero = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=256, null=False, unique=True)
    candidatos = models.ManyToManyField(Candidato)

    def __str__(self):
        return '{0}'.format(self.nombre)


class Usuario (models.Model):
    identificacion = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=256, verbose_name='Nombre Completo')
    genero = models.CharField(max_length=20, choices=[('Masculino', 'M'), ('Femenino', 'F')])
    fecha_nacimiento = models.DateField()
    sucursal = models.ForeignKey(Sucursal)

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.identificacion)


class Voto (models.Model):
    hora_inicio = models.DateTimeField(verbose_name= 'Hora de inicio')
    hora_fin = models.DateTimeField(verbose_name= 'Hora de fin')
    usuario = models.ForeignKey(Usuario)
    lista_electoral = models.ForeignKey(ListaElectoral)
    candidato_seleccionado = models.ForeignKey(Candidato)
    activo = models.BooleanField()

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.usuario, self.lista_electoral, self.activo)



