from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Sukursime autoserviso appsa')

def index1(request):
    return HttpResponse('Testuojame')
