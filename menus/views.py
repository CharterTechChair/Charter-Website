import datetime

# Some standard stuff from the Django Library
from django import template
#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Forms and Models
from menus.models import MenuItem
from menus.forms import MenuForm

from charterclub.permissions import render
from charterclub import permissions

@permissions.officer
def menu_input(request):
   now = datetime.datetime.now().date()
   #Generate Event Form
   if request.method == 'POST':
     form = MenuForm(request.POST)
     if form.is_valid():
        data = form.cleaned_data

        lookup = MenuItem.objects.filter(date=data['date'])

        if not lookup:
          menuitem = MenuItem(date=data['date'], 
                            lunch_food=data['lunch_food'],
                            dinner_food=data['dinner_food'])
          menuitem.save()
        else:
          menuitem = lookup[0]
          menuitem.lunch_food = data['lunch_food']
          menuitem.dinner_food = data['dinner_food']
          menuitem.save()

        return HttpResponseRedirect('view') # Redirect after POST
   else:
      form = MenuForm()

   return render(request, 'menu_input.html', {
     'form': form,
     'error': '',
     'netid':  permissions.get_username(request),
   })  

def menu(request):
   now = datetime.datetime.now().date()

   startdate = datetime.date.today()
   enddate = startdate + datetime.timedelta(days = 7)
   mlist = MenuItem.objects.filter(date__range=[startdate, enddate]).order_by('date')

   return render(request, 'menu.html', {
     'error': '',
     'netid': permissions.get_username(request),
     'menu_list': mlist ,
   })  
