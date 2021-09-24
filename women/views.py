from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка women.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статті по категоріях</h1><p>{catid}</p>")


def archive(request, year):
    if (int(year) > 2021):
        raise Http404()
    return HttpResponse(f"<h1>Архів по рокам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')