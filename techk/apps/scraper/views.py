# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.scraper.scrap import scraping
from apps.base.models import Categories, Books
from django.urls import reverse

# Create your views here.
def procesar(request):
    # 1- correr el scraper
    mensaje = scraping()
    if mensaje == 'Proceso Exitoso!':
        # 2- traer las categorias
        categories = Categories.objects.all()
        # 3- listar las categorias con link para ver mas detalles
    else:
        categories = None

    context = {
        'categories' : categories
    }
    return render(request,'categories.html',context)

def book_list(request,pk):
    print(pk)
    category_id = Categories.objects.get(id=pk)
    print(category_id)
    books = Books.objects.filter(category_id=category_id)

    context = {
        'books' : books
    }

    return(request,'books.html',context)
    # return HttpResponse('Hello, world!')

def delete(request,pk):
    print('aqui')

    book = Books.objects.get(id=pk)
    # category_id = book.category_id.category_id.id
    book.delete()

    # return redirect(reverse('scraper:book_list',kwargs={'pk':category_id}))
    return render(request,'index.html')
