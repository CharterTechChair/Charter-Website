from charterclub.views import render
import charterclub.permissions as permissions

from charterclub.models import Prospective

from kitchen.models import Meal, Brunch, Lunch, Dinner
from kitchen.forms import MealSignupForm

from django.utils import timezone

import datetime

# Displays the weekly menu for this week
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

    # Look at the meals in the future
    future_meals =  Meal.objects.filter(day__gte=timezone.now())
    future_dates = sorted(set([m.day for m in future_meals]))
 
    # Figure out which ones are available
    available_dates = []
    calendar_date_to_text = {}
    for d in future_dates:
        m_a =  [m.cast() for m in Meal.objects.filter(day=d)]

        hover_text = []

        for m in m_a:
            # i.e. Brunch: 20/30
            name = m.__class__.__name__
            num_attending = len(m.meals_attended.all())
            num_limit = m.sophomore_limit
            hover_text.append("%s: %s/%s" % (name, num_attending, num_limit))
            
            if num_attending < num_limit:
                available_dates.append(d)

        calendar_date_to_text[d.strftime("%Y-%m-%d")] = ",".join(hover_text)
        
    # Which days can the choose on the calender picker?
    dates_allowed = sorted(set([d.strftime("%Y-%m-%d") for d in available_dates]))

        
    return render(request, 'kitchen/meal_signup.html', 
        {
            "prospective" : prospective,
            'form': form,
            'dates_allowed' : dates_allowed,
            'hover_text' : calendar_date_to_text,
        })
