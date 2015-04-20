from django.http import HttpResponse
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings
from datetime import date
from os import listdir, path

def index(request):
   html = "Hello World"
   return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
   return render(request, "calendar.html")
   # return HttpResponse("This is a completely functional calendar")


   
def faceboard(request):
   def picsfromyear(year):
      piclocation = "static/img/faceboard/"
      pics = []
      if not path.exists(piclocation + str(year)):
         return
      
      for pic in listdir(piclocation + str(year)):
         pics.append(str(year) + "/" + pic)
      return pics
            
   year = date.today().year
   template = get_template("faceboard.html")
   seniorpics = picsfromyear(year)
   juniorpics = picsfromyear(year + 1)
   sophpics = picsfromyear(year + 2)
   context = RequestContext(request,
                            {"seniorpics" : seniorpics,
                             "juniorpics" : juniorpics,
                             "sophpics" : sophpics})
   return HttpResponse(template.render(context))
   
def menu(request):
   return render(request, "menu.html")
   # return HttpResponse("This is a completely functional menu")

def history(request):
   return render(request, "history.html")

def song(request):
   return render(request, "song.html")

def constitution(request):
   return render(request, "constitution.html")

def profile(request):
  return render(request, "profile.html")

def login(request):
   return HttpResponse("This is a completely functional CAS login page")

def help(request):
   return HttpResponse("This is under construction!")

def underconstruction(request):
   return HttpResponse("This is under construction!")

