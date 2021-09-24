from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка women.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статті по категоріях</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архів по рокам</h1>{year}</p>")
