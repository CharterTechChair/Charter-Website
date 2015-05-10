import datetime

# Some standard stuff from the Django Library
from django import template
#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Forms and Models
from menus.models import MenuItem
from menus.forms import MenuForm

from charterclub.views import render

def menu_input(request):
   now = datetime.datetime.now().date()
   #Generate Event Form
   if request.method == 'POST':
     form = MenuForm(request.POST)
     if form.is_valid():
        data = form.cleaned_data

#         menuitem = MenuItem(day=data['day'], date=data['date'], 
        menuitem = MenuItem(day=data['day'], 
                             lunch_food=data['lunch'], dinner_food=data['dinner'])
        menuitem.save()

        return HttpResponseRedirect('menu') # Redirect after POST
   else:
      form = MenuForm()

   return render(request, 'menu_input.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': 'roryf',
     # 'netid': request.user.username,
   })  

def menu(request):
  # NEED TO COME UP WITH A MORE ELEGANT WAY TO DO THIS WITH TWO COLUMNS

   # return render(request, "menu.html")
   # return HttpResponse("This is a completely functional menu")
   now = datetime.datetime.now().date()

   startdate = datetime.date.today() - datetime.timedelta(days=3)
   enddate = startdate + datetime.timedelta(weeks=1)
   mlist = MenuItem.objects.all()
   # mlist = MenuItem.objects.order_by('day')
   # mlist = MenuItem.objects.filter(date__range=[startdate, enddate]).order_by('date')

   return render(request, 'menu.html', {
     'current_date': now,
     'error': '',
     'netid': 'quanzhou',
     'menu_list': mlist ,
   })  
