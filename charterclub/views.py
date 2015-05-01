from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings
import datetime
from forms import *
# import configuration
from os import listdir, path
from django.core.mail import send_mail, BadHeaderError

import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response

from models import *


def index(request):
   html = "Hello World"
   return render(request, "index.html")
#    return HttpResponse(html)

def calendar(request):
   return render(request, "calendar.html")
   # return HttpResponse("This is a completely functional calendar")

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

def feedback(request):
   now = datetime.datetime.now().date()
   #Generate Meal Form
   if request.method == 'POST':
     form = FeedbackForm(request.POST)
     if form.is_valid():
        subject = 'Anonymous Feedback'
        message = form.cleaned_data['anonymous_feedback']
        sender = 'roryf@princeton.edu'
        # cc_myself = form.cleaned_data['cc_myself']

        recipients = ['roryf@princeton.edu']
        # if cc_myself:
        #     recipients.append(sender)

        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients, fail_silently=False)
        return HttpResponseRedirect('thanks') # Redirect after POST
   else:
      form = FeedbackForm()

   return render(request, 'feedback.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': request.user.username,
   })  

def winetasting(request):
   now = datetime.datetime.now().date()
   #Generate Meal Form
   if request.method == 'POST':
     form = WinetastingForm(request.POST)
     # if form.is_valid():

   else:
      form = WinetastingForm()

   return render(request, 'feedback.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': request.user.username,
   })  


def winetasting_view(request):
   now = datetime.datetime.now().date()

   wt_obj = Event.objects.filter(title='Winetasting')[0]

   return render(request, 'winetasting_view.html', {
     'current_date': now,
     'error': '',
     'netid': 'quanzhou',
     'room_list' : wt_obj.to_JSON()['rooms'],
   })  


def menu(request):
   return render(request, "menu.html")
   # return HttpResponse("This is a completely functional menu")

def history(request):
   return render(request, "history.html")

def song(request):
   return render(request, "song.html")

def constitution(request):
   return render(request, "constitution.html")

def thanks(request):
  now = datetime.datetime.now().date()
  return render(request, "thanks.html", {
     'current_date': now,
     'error': '',
     'netid': request.user.username,
  })

def profile(request):
  now = datetime.datetime.now().date()
  return render(request, "profile.html", {
     'current_date': now,
     'error': '',
     'netid': request.user.username,
  })

# def login(request):
#    return HttpResponse("This is a completely functional CAS login page")

def help(request):
   return HttpResponse("This is under construction!")

def underconstruction(request):
   return HttpResponse("This is under construction!")
