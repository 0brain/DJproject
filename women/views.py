from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["Про сайт", "Додати статтю", "Зворотній зв'язок", "Увійти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторінка'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Про сайт'})


def categories(request, catid):
    return HttpResponse(f"<h1>Статті по категоріях</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2021:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архів по рокам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')