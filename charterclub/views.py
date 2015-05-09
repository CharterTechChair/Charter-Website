from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings

import datetime
from forms import *
from events.models import *
# import configuration
from os import listdir, path
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone

import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response

from models import *
import permissions

def index(request):
    html = "Hello World"
    return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
    # return render(request, "calendar.html")
    # return HttpResponse("This is a completely functional calendar")
    now = datetime.datetime.now().date()

    startdate = date.today() - timedelta(days=1)
    enddate = startdate + timedelta(weeks=52)
    elist = SocialEvent.objects.filter(date_and_time__range=[startdate, enddate]).order_by('date_and_time')

    return render(request, 'calendar.html', {
     'current_date': now,
     'error': '',
     'netid': 'quanzhou',
     'events_list': elist ,
    })  

def calendar2(request):
   return render(request, "calendar2.html")
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
              
    year = datetime.date.today().year
    template = get_template("faceboard.html")
    seniorpics = picsfromyear(year)
    juniorpics = picsfromyear(year + 1)
    sophpics = picsfromyear(year + 2)
    context = RequestContext(request,
                             {"seniorpics" : seniorpics,
                              "juniorpics" : juniorpics,
                              "sophpics" : sophpics})
    return HttpResponse(template.render(context))
   
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def history(request):
   return render(request, "history.html")

def song(request):
   return render(request, "song.html")

def constitution(request):
   return render(request, "constitution.html")

def hello(request):
  now = datetime.datetime.now().date()
  return render(request, "hello.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
  })

@permissions.member
def profile(request):
  
  now = datetime.datetime.now().date()

  # m = Member.objects.filter(netid=request.user.username)
  m = Member.objects.filter(netid=permissions.get_username(request))[0]
  # m = Member.objects.filter(netid='roryf')

  e = m.get_events()
  # house_account = m.house_account
  # officer = m.position
  # year = m.year

  return render(request, "profile.html", {
     'current_date': now,
     'error': '',
     'member': m,
     'events': e,
     'netid': permissions.get_username(request)
     # 'netid': 'roryf'
  })

@permissions.officer
def officer(request):
  m = Member.objects.filter(netid=permissions.get_username(request))[0]

  return render(request, "officer.html", {
  'member': m
  })

# def login(request):
#    return HttpResponse("This is a completely functional CAS login page")

def permission_denied(request):
    return render(request, "permission_denied.html")

def help(request):
   return HttpResponse("This is under construction!")

def underconstruction(request):
   return HttpResponse("This is under construction!")
