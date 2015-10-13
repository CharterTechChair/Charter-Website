from django.db import models
from django.utils import timezone

from events.models import Entry
from charterclub.models import limit_meals_attended_choices


class ProspectiveMealEntry(models.Model):
    '''
        Models a sophomore meal. 
    '''
    prospective = models.ForeignKey("charterclub.Prospective")
    meal = models.ForeignKey("kitchen.Meal", limit_choices_to=limit_meals_attended_choices)
    completed = models.BooleanField("Has this person completed the meal?", default=False)
    signup_date = models.DateField(blank=True, default=timezone.now().date())
    points = models.DecimalField("Number of points this event is worth", default=1, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s for %s" % (self.prospective, self.meal)

class ProspectiveEventEntry(Entry):
    '''
        Models a recruitment event where we have to make 
    '''
    completed = models.BooleanField("Has this person attended this event?", default=False)
    signup_date = models.DateField(blank=True, default=timezone.now().date())
    points = models.DecimalField("Number of points this event is worth", default=1, max_digits=5, decimal_places=2)