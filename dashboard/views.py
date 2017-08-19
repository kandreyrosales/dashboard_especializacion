# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Voto, ListaElectoral
from django.shortcuts import render
from django.views import generic
from django.db.models import Count


class VotoListView(generic.ListView):
    model = Voto
    context_object_name = 'voto_list'   # your own name for the list as a template variable
    queryset = Voto.objects.filter(lista_electoral__numero=121) # Get 5 books containing the title war
    template_name = 'ticket/ticket_list.html'  # Specify your own template name/location

    def get_context_data(self,**kwargs):
        context = super(VotoListView,self).get_context_data(**kwargs)
        context['votos_invalidos'] = Voto.objects.filter(lista_electoral__numero=121, activo=False).count()
        vt = Voto.objects.values('candidato_seleccionado__nombre').order_by().annotate(Count('id'))
        context['votantes_validos'] = vt
        return context
