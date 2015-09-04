from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_choices = (('Lunch', 'Lunch'),
                    ('Dinner', 'Dinner'))

    # Fields of this object
    day             = models.DateField()
    meals           = models.CharField(max_length=10, choices=meal_choices)
    allow_sophomore = models.BooleanField(default=False)
    name            = models.CharField(max_length=100, blank=True, null=True, help_text="Optional Name")
    
    description    = models.TextField(max_length=1000, help_text="What are we eating today?")
    # For Lunch 
    grill          = models.CharField(max_length=1000, null=True, blank=True, help_text="Visible only for Lunches")
    # For dinner
    plated_option = models.CharField(max_length=1000, null=True, blank=True, help_text="Visible only for Dinners")

    # For both
    salad          =  models.CharField(max_length=1000, blank=True, help_text="For Herbivores")
    special_note    = models.CharField(max_length=1000, null=True, blank=True, help_text="i.e. 'Seniors only', or 'Meal ends early at 7:00pm'")


    def __unicode__(self):
        return "%s %s" % (self.day.strftime("%a %m/%d/%y"), self.meals)

