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
    has_been_checked = models.BooleanField("Has an officer checked this meal or not?", default=False)
    points = models.DecimalField("Number of points this event is worth", default=1, max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-meal']

    def __unicode__(self):
        return "%s for %s" % (self.prospective, self.meal)

    # @property
    # def sorted_prospectivemealentry_set(self):
    #     return self.prospectivemealentry_set.order_by('day')

class ProspectiveEventEntry(Entry):
    '''
        Models a recruitment event where we have to make 
    '''
    completed = models.BooleanField("Has this person attended this event?", default=False)
    has_been_checked = models.BooleanField("Has an officer checked this prospective into this event?", default=False)
    signup_date = models.DateField(blank=True, default=timezone.now().date())
    points = models.DecimalField("Number of points this event is worth", default=1, max_digits=5, decimal_places=2)