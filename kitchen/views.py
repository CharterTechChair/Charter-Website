from charterclub.views import render
import charterclub.permissions as permissions

from charterclub.models import Prospective

from kitchen.models import Meal
from django.utils import timezone

import datetime

# Displays the weekly menu for this week
@permissions.member
def weekly_menu(request):
    # Find the relevant days
    today = timezone.now()
    monday = (today + datetime.timedelta(days=-today.weekday(), weeks=0)).date()
    week = [monday + datetime.timedelta(days=i) for i in range(0,7)]
    
    meals_iter = []
    # Find the proper meals
    for day in week:
        brunch = Meal.objects.filter(day=day, meals="Brunch") 
        lunch = Meal.objects.filter(day=day, meals="Lunch")
        dinner = Meal.objects.filter(day=day, meals="Dinner")

        # Dereference the hits
        if lunch:
            lunch = lunch[0]
        if dinner:
            dinner = dinner[0]
        if brunch:
            brunch = brunch[0]

        name = day.strftime("%a %m/%d")
        
        # Prevent both brunch and lunch from showing up, which screws up formatting
        if brunch:
            lunch = None        
        meals_iter.append((name, day, brunch, lunch, dinner))

    return render(request, 'kitchen/weekly_menu.html', {
        'meals_week' : meals_iter,
    })

# Uses a calender widget to sign up for meals
@permissions.prospective
def meal_signup(request):
    netid = permissions.get_username(request)
    prospective = Prospective.objects.filter(netid=netid)[0]

    return render(request, 'kitchen/meal_signup.html', 
        {
            "prospective" : prospective,
        })
