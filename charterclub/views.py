from django.http import HttpResponse
from django import template
from django.shortcuts import render

def index(request):
   html = "Hello World"
   return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
   return render(request, "calendar.html")
   # return HttpResponse("This is a completely functional calendar")

def menu(request):
   return render(request, "menu.html")
   # return HttpResponse("This is a completely functional menu")

def history(request):
   return HttpResponse("This is a completely functional history")

def song(request):
   return HttpResponse("This is a completely functional song")

def constitution(request):
   return HttpResponse("This is a completely functional constitution")

def underconstruction(request):
   return HttpResponse("This is a under construction!")

