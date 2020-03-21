from django.shortcuts import render
from django.http import HttpResponse


def hello(request): 
    oi = '<h1>Hello Arthur</h1>'
    return HttpResponse(oi)
