from django.http import HttpResponse
from django import template
from django.shortcuts import render

def index(request):
    html = "Hello World"
    return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
    return "This is a completely functional calendar"

def menu(request):
    return "This is a completely functional menu"

def history(request):
    return "This is a completely functional history"

def song(request):
    return "This is a completely functional song"

def constitution(request):
    return "This is a completely functional constitution"

def underconstruction(request):
    return "This feature is not functional at all"
