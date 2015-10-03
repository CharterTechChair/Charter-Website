from django.db import models
from django.utils import timezone

# Create your models here.
class ProspectiveMealEntry(models.Model):
    prospective = models.ForeignKey("charterclub.Prospective")
    meal = models.ForeignKey("kitchen.Meal")
    completed = models.BooleanField("Has this person completed the meal", default=False)
    signup_date = models.DateField(blank=True, default=timezone.now().date())