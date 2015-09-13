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
from permissions import render

from ldap_student_lookup import get_student_info



########################################################################
# Some easy one-age requests
# 
# Displays the membership of a target year
########################################################################
def index(request):
    return render(request, "index.html")


def history(request):
    return render(request, "flatpages_default/history.html")

def song(request):
    return render(request, "flatpages_default/song.html")

def constitution(request):
    return render(request, "flatpages_default/constitution.html")



def catering(request):
    manager = Staff.objects.all().order_by('order')

    if manager:
        manager = manager[0]
    else:
        manager = None

    return render(request, "charterclub/pages/catering.html", {
          'manager' : manager,
      })

# allow user to view list of current officer corps.
def officer_list(request):

    olist = Officer.objects.all()

    query_s = Officer.objects.filter(is_active=True).order_by('order')
    top6 = query_s[:6]
    officer_rest = query_s[6:]

    return render(request, 'charterclub/officer_list.html', {
       'title' : 'Our Undergraduate Officers',
       'top6' : top6,
       'officer_rest' : officer_rest
    }) 

# allow user to view list of current officer corps.
def staff_list(request):
    olist = Staff.objects.all()

    query_s = Staff.objects.filter().order_by('order')
    top6 = query_s[:6]
    staff_rest = query_s[6:]

    return render(request, 'charterclub/officer_list.html', {
     'title' : 'Our Staff',
     'top6' : top6,
     'officer_rest' : staff_rest
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
     'netid': permissions.get_username(request),
     'prez': prez,
     'vp': vp,
    }) 


########################################################################
# Faceboard
# 
# Displays the current membership
########################################################################
def faceboard(request):
    # rollover = June 3nd
    senior_year = (date.today() - timedelta(days=153)).year + 1

    current_membership = Member.objects.filter(year__range=(senior_year, senior_year+2))

    year_options = Member.get_membership_years()

    return render(request, 'charterclub/faceboard.html', {
      'title':   'Current Membership',
      'year_options': reversed(year_options),
      'display_membership' : current_membership,
  })

########################################################################
# Faceboard_year
# 
# Displays the membership of a target year
########################################################################
def faceboard_year(request, year):
    # rollover = June 3nd
    members = Member.objects.filter(year=year)

    year_options = Member.get_membership_years()

    return render(request, 'charterclub/faceboard.html', {
      'title':   'Class of %s' % year,
      'year_options': reversed(year_options),
      'display_membership' : members,
    })

# greeting page
@permissions.member
def hello(request):
    now = datetime.datetime.now().date()
    
    m = Member.objects.filter(netid=permissions.get_username(request))[0]

    return render(request, "hello.html", {
       'current_date': now,
       'm': m,
       'netid': permissions.get_username(request),
    })



# Allows a member or a prospective to view their page
# DO NOT use the decorator permissions.member or permissions.prospective on this
#    The logic in this function will verify this information
def profile(request):
    # check their permissions
    netid_s = permissions.get_username(request)

    # Reject them if not valid netid
    if not netid_s:
      return render(request, "permission_denied.html",
              {"required_permission": "member or prospective"}) 

    # Do lookups in the database
    m_query = Member.objects.filter(netid=netid_s)
    p_query = Prospective.objects.filter(netid=netid_s)

    # Show prospective page
    if p_query:
              return render(request, "charterclub/prospective_profile.html", {
            'member': p_query[0],
            # 'events': e,
            'netid': permissions.get_username(request)
        })
              
    # Show members page 
    if m_query:
        return render(request, "charterclub/member_profile.html", {
            'member': m_query[0],
            # 'events': e,
            'netid': permissions.get_username(request)
        })


    return render(request, "permission_denied.html",
                  {"required_permission": "member or prospective"})

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
       'netid': permissions.get_username(request),
     })  

# view the list of people who have signed up for our mailing list.
# should probably implement an actual listserv of some description
# at some point
@permissions.officer
def mailinglist_view(request):
    plist = Prospective.objects.all()

    return render(request, "mailinglist_view.html", {
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
