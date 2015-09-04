from charterclub.views import render
import charterclub.permissions as permissions

from kitchen.models import Meal
from django.utils import timezone

import datetime

# Create your views here.
@permissions.member
def weekly_menu(request):
    # Find the relevant days
    today = timezone.now()
    monday = (today + datetime.timedelta(days=-today.weekday(), weeks=0)).date()
    week = [monday + datetime.timedelta(days=i) for i in range(0,7)]
    
    meals_iter = []
    # Find the proper meals
    for day in week:
        lunch = Meal.objects.filter(day=day, meals="Lunch")
        dinner = Meal.objects.filter(day=day, meals="Dinner")

        # Dereference the hits
        if lunch:
            lunch = lunch[0]
        if dinner:
            dinner = dinner[0]

        name = day.strftime("%a %m/%d")
        
        meals_iter.append((name, day, lunch, dinner))

    return render(request, 'kitchen/weekly_menu.html', {
        'meals_week' : meals_iter,
      # 'title':   'Class of %s' % year,
      # 'year_options': reversed(year_options),
      # 'display_membership' : members,
      # 'member':   Member.objects.filter(netid=permissions.get_username(request))[0]
    })