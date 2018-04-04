from django.db import models
from django.utils import timezone

from events.models import Entry
from charterclub.models import limit_meals_attended_choices

import urllib

class ProspectiveMealEntry(models.Model):
    '''
        Models a sophomore meal. 
    '''
    prospective = models.ForeignKey("charterclub.Prospective")
    meal = models.ForeignKey("kitchen.Meal", limit_choices_to=limit_meals_attended_choices)
    completed = models.BooleanField("Has this person completed the meal?", default=False)
    signup_date = models.DateField(blank=True, auto_now_add=True)
    points = models.DecimalField("Number of points this meal is worth", default=1, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s for %s" % (self.prospective, self.meal)

    def cancellation_url(self):
        base_url='kitchen/meal_cancellation/'
        url = base_url + "%s/%s/%s/%s" % (self.id,self.prospective.id, self.meal.cast().__class__.__name__, self.signup_date.isoformat())
        return urllib.quote(url)

    def can_be_cancelled_by_user(self):
        return self.meal.day > timezone.now().date()

class ProspectiveEventEntry(Entry):
    '''
        (Not used yet)
    '''
    completed = models.BooleanField("Has this person attended this event?", default=False)
    signup_date = models.DateField(blank=True, auto_now_add=True)
    points = models.DecimalField("Number of points this event is worth", default=1, max_digits=5, decimal_places=2)