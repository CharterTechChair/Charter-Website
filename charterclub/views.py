from django.http import HttpResponse
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings
from os import listdir

def index(request):
   html = "Hello World"
   return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
   return render(request, "calendar.html")
   # return HttpResponse("This is a completely functional calendar")

def faceboard(request):
   template = get_template("faceboard.html")
   context = RequestContext(request,
                            {"pics" : listdir("static/img/faceboard")})
   return HttpResponse(template.render(context))
   
def menu(request):
   return HttpResponse("This is a completely functional menu")

def history(request):
   return HttpResponse("This is a completely functional history")

def song(request):
   return HttpResponse("This is a completely functional song")

def constitution(request):
   return HttpResponse("This is a completely functional constitution")

def underconstruction(request):
   return HttpResponse("This is a under construction!")

