from django.http import HttpResponse, HttpResponseRedirect
from django import template
import django.shortcuts
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

from ldap_student_lookup import get_student_info

def additional_context(request):
    netid = permissions.get_username(request)
    
    o = Officer.objects.filter(netid=netid)
    if len(o) > 0:
        o = o[0]
    else:
        o = None

    if not o:
        m = Member.objects.filter(netid=netid)
        if len(m) > 0:
            m = m[0]
        else:
            m = None
    else:
        m = o

    if not m:
        if not netid == "":
            s = get_student_info(netid)
        else:
            s = None
    else:
        s = m   
    
    return {"member" : m, "student" : s, "officer" : o}

# a replacement render function which passes some additional
# user information to our template by wrapping the original
# render function. specifically, it passes information about the
# student/member/officer status of the user.
def render(request, template_name, context=None, *args, **kwargs):
    add_context = additional_context(request)
    if context:
        add_context.update(context)

    return django.shortcuts.render(request, template_name, add_context,
                                   *args, **kwargs)

def index(request):
    html = "Hello World"
    return render(request, "index.html")
#    return HttpResponse(html)
 
@permissions.member   
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
    seniorpics = picsfromyear(year)
    juniorpics = picsfromyear(year + 1)
    sophpics = picsfromyear(year + 2)

    return render(request, 'faceboard.html', {
      'seniorpics': seniorpics,
      'juniorpics': juniorpics,
      'sophpics': sophpics,
      'netid': permissions.get_username(request)
  })

def history(request):
   return render(request, "history.html")

def song(request):
   return render(request, "song.html")

def constitution(request):
   return render(request, "constitution.html")

@permissions.member 
def officer_list(request):
    now = datetime.datetime.now().date()

    olist = Officer.objects.all()

    return render(request, 'officer_list.html', {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
     'officerlist': olist ,
    }) 

def contactus(request):
    now = datetime.datetime.now().date()

    prez = Officer.objects.filter(position='President')
    vp = Officer.objects.filter(position='Vice President')

    if not prez: 
      prez = ''
    else:
      prez = prez[0]


    if not vp:
      vp = ''
    else:
      vp = vp[0]


    return render(request, 'contactus.html', {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
     'prez': prez,
     'vp': vp,
    }) 

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

  m = Member.objects.filter(netid=permissions.get_username(request))[0]

  e = m.get_events()

  return render(request, "profile.html", {
     'current_date': now,
     'error': '',
     'member': m,
     'events': e,
     'netid': permissions.get_username(request)
  })

@permissions.officer
def officer(request):
  m = Member.objects.filter(netid=permissions.get_username(request))[0]

  return render(request, "officer.html", {
  'member': m
  })

def mailinglist(request):
  if request.method == 'POST':
    form = MailingListForm(request.POST)
    if form.is_valid():
      form.add_soph()

      return HttpResponseRedirect('contactus')
        
  else:
    form = MailingListForm()


  return render(request, 'mailinglist.html', {
     'form': form,
     'error': '',
     'netid': permissions.get_username(request),
   })  

def mailinglist_view(request):
  plist = Prospective.objects.all()

  return render(request, "mailinglist_view.html", {
     'error': '',
     'plist': plist,
     'netid': permissions.get_username(request)
  })

def permission_denied(request):
    return render(request, "permission_denied.html")

def underconstruction(request):
  return render(request, "underconstruction.html", {
  })

def error404(request):
    return render(request, "404.html")
