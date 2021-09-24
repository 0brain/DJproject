from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка women.")


def categories(request):
    return HttpResponse("<h1>Статті по категоріях</h1>")
