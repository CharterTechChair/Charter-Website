from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.conf import settings
import datetime
from forms import FeedbackForm
# import configuration
from os import listdir, path
from django.core.mail import send_mail, BadHeaderError

import time
import calendar
# from datetime import date, datetime, timedelta

# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
# from django.core.context_processors import csrf
# from django.forms.models import modelformset_factory

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
   
# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

def feedback(request):
   now = datetime.datetime.now().date()
   #Generate Meal Form
   if request.method == 'POST':
     form = FeedbackForm(request.POST)
     if form.is_valid():
        subject = 'Anonymous feedback'
        sender = 'roryf@princeton.edu'
        message = form.cleaned_data['anonymous_feedback']

        recipients = ['roryf@princeton.edu']

        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)
        # return HttpResponseRedirect('/thanks/') # Redirect after POST
   else:
      form = FeedbackForm()

   return render(request, 'feedback.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': request.user.username,
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

def profile(request):
  return render(request, "profile.html")

def login(request):
   return HttpResponse("This is a completely functional CAS login page")

def help(request):
   return HttpResponse("This is under construction!")

def underconstruction(request):
   return HttpResponse("This is under construction!")

# # TEST CODE FOR CALENDAR!!!
# mnames = "January February March April May June July August September October November December"
# mnames = mnames.split()


# # @login_required
# def cal(request, year=None):
#     """Main listing, years and months; three years per page."""
#     # prev / next years
#     if year: year = int(year)
#     else:    year = time.localtime()[0]

#     nowy, nowm = time.localtime()[:2]
#     lst = []

#     # create a list of months for each year, indicating ones that contain entries and current
#     for y in [year, year+1, year+2]:
#         mlst = []
#         for n, month in enumerate(mnames):
#             entry = current = False   # are there entry(s) for this month; current month?
#             entries = Entry.objects.filter(date__year=y, date__month=n+1)
#             if entries:
#                 entry = True
#             if y == nowy and n+1 == nowm:
#                 current = True
#             mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
#         lst.append((y, mlst))

#     return render_to_response("cal.html", dict(years=lst, user=request.user, year=year,
#                                                    reminders=reminders(request)))


