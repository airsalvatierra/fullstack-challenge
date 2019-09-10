# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def procesar(request):
    # 1- correr el scraper
    # 2- traer las categorias
    # 3- listar las categorias con link para ver mas detalles
    return HttpResponse('procesando')
