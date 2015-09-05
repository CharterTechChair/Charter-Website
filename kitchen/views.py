from charterclub.views import render
import charterclub.permissions as permissions

from charterclub.models import Prospective

from kitchen.models import Meal, Brunch, Lunch, Dinner
from kitchen.forms import MealSignupForm

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
        brunch = Brunch.objects.filter(day=day) 
        lunch = Lunch.objects.filter(day=day)
        dinner = Dinner.objects.filter(day=day)

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

    # Give them a form to fill out
    if request.method == 'POST':
        form = MealSignupForm(request.POST)
        if form.is_valid():
            form.add_soph()
    else:
        form = MealSignupForm()

    dates_allowed = ['2015-09-05']

    # Look at the meals in the future
    available_meals =  Meal.objects.filter(day__gte=timezone.now())
    available_days = sorted(set([m.day for m in available_meals]))
    slots_taken = [len(m.meals_attended.all()) for m in available_meals]
    limit = [m.sophomore_limit for m in available_meals]

    #Now pass these values to the javascript function in the template
    dates_allowed = [d.strftime("%Y-%m-%d") for d in available_days]

    return render(request, 'kitchen/meal_signup.html', 
        {
            "prospective" : prospective,
            'form': form,
            'dates_allowed' : dates_allowed,
        })
