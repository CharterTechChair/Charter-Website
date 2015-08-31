from django.http import HttpResponse, HttpResponseRedirect
from django import template
import django.shortcuts
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings

import datetime
from datetime import date, timedelta

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


# build context data concerning the user associated with request
# this includes a representation of them as a student, member, and officer
# if applicable
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
    return render(request, "index.html")


########################################################################
# Faceboard
# 
# Displays the current membership
########################################################################
@permissions.member   
def faceboard(request):
    # rollover = June 3nd
    senior_year = (date.today() - timedelta(days=153)).year + 1

    current_membership = Member.objects.filter(year__range=(senior_year, senior_year+2))

    year_options = Member.get_membership_years()

    return render(request, 'charterclub/faceboard.html', {
      'title':   'Current Membership',
      'year_options': reversed(year_options),
      'display_membership' : current_membership,
      'member':   Member.objects.filter(netid=permissions.get_username(request))[0]
  })

########################################################################
# Faceboard_year
# 
# Displays the membership of a target year
########################################################################

@permissions.member
def faceboard_year(request, year):
    # rollover = June 3nd
    members = Member.objects.filter(year=year)
    
    year_options = Member.get_membership_years()

    return render(request, 'charterclub/faceboard.html', {
      'title':   'Class of %s' % year,
      'year_options': reversed(year_options),
      'display_membership' : members,
      'member':   Member.objects.filter(netid=permissions.get_username(request))[0]
  })

def history(request):
   return render(request, "history.html")

def song(request):
   return render(request, "song.html")

def constitution(request):
   return render(request, "constitution.html")

# allow user to view list of current officer corps.
@permissions.member 
def officer_list(request):
    now = datetime.datetime.now().date()

    olist = Officer.objects.all()

    return render(request, 'charterclub/officer_list.html', {
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

# greeting page
@permissions.member
def hello(request):
  now = datetime.datetime.now().date()
  
  m = Member.objects.filter(netid=permissions.get_username(request))[0]

  return render(request, "hello.html", {
     'current_date': now,
     'error': '',
     'm': m,
     'netid': permissions.get_username(request),
  })

# allows a member to view their own user profile
@permissions.member
def profile(request):
  
  now = datetime.datetime.now().date()

  m = Member.objects.filter(netid=permissions.get_username(request))[0]

  e = m.get_events()

  return render(request, "charterclub/profile.html", {
     'current_date': now,
     'error': '',
     'member': m,
     'events': e,
     'netid': permissions.get_username(request)
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

# view the list of people who have signed up for our mailing list.
# should probably implement an actual listserv of some description
# at some point
@permissions.officer
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
