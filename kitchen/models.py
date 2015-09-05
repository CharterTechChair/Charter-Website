from django.db import models

# Create your models here.
class Meal(models.Model):
    display_name = "Meal"
    # Fields of this object
    day             = models.DateField()
    sophomore_limit  = models.IntegerField(default=0, help_text="Put '0' to not allow sophomores")
    name            = models.CharField(max_length=100, blank=True, help_text="Optional Name")
    description    = models.TextField(max_length=1000, help_text="What are we eating today?")
    special_note    = models.CharField(max_length=1000, blank=True, help_text="Optoinal note- i.e. 'Seniors only', or 'Meal ends early at 7:00pm'")


    def __unicode__(self):
        return "%s %s" % (self.day.strftime("%m/%d/%y %a"), self.display_name)



    # def html(self):
    #     '''
    #         Returns the meal, formatted as div.
    #     '''

    #     return '''
    #         <div> %s 
    #     '''
class Brunch(Meal):
    display_name = "Brunch"
    grill_special = models.CharField(max_length=1000, blank=True, help_text="Optional")
    omlette = models.CharField(max_length=1000, blank=True, help_text="Optional")



class Lunch(Meal):
    display_name = "Lunch"
    grill_special = models.CharField(max_length=1000, blank=True, help_text="Optionals")
    salad          =  models.CharField(max_length=1000, blank=True, help_text="Optional")

class Dinner(Meal):
    display_name = "Dinner"
    plated_option = models.CharField(max_length=1000, blank=True, help_text="Optional")
    salad         =  models.CharField(max_length=1000, blank=True, help_text="Optional")
