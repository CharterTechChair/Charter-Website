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
         soph, error_message = createSophomore(request.user.username, form.cleaned_data['first_name'], form.cleaned_data['last_name'])
         if error_message:
             return render(request, 'feedback.html', {
                 'current_date': now,
                 'form': form,
                 'error': "Error: " + error_message,
                 'netid': request.user.username,
             })

         # Once we have ThisSophmore, sign him up for the meal.
         error_message = soph.sign_up(form.cleaned_data['date'], form.cleaned_data['lunch_or_dinner'])

         if not error_message:
             return HttpResponseRedirect('mealview')
         else:
             return render(request, 'feedback.html', {
                 'current_date': now,
                 'form': form,
                 'error': error_message,
                 'netid': request.user.username,
             })
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

