from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.db import models

# Taken from: http://stackoverflow.com/questions/929029/how-do-i-access-the-child-classes-of-an-object-in-django-without-knowing-the-name/929982#929982
class InheritanceCastModel(models.Model):
    """
    An abstract base class that provides a ``real_type`` FK to ContentType.

    For use in trees of inherited models, to be able to downcast
    parent instances to their child types.

    """
    real_type = models.ForeignKey(ContentType, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(InheritanceCastModel, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)

    class Meta:
        abstract = True

# Create your models here.
class Meal(InheritanceCastModel):
    display_name = "Meal"
    # Fields of this object
    day             = models.DateField()
    sophomore_limit  = models.IntegerField(default=0, help_text="Put '0' to not allow sophomores")
    name            = models.CharField(max_length=100, blank=True, help_text="Optional Name")
    description    = models.TextField(max_length=1000, help_text="What are we eating today?")
    special_note    = models.CharField(max_length=1000, blank=True, help_text="Optoinal note- i.e. 'Seniors only', or 'Meal ends early at 7:00pm'")


    def __unicode__(self):
        return "%s %s" % (self.day.strftime("%m/%d/%y %a"), self.display_name)


    def num_of_sophomores(self):
        '''
            Number of sophomores eating here
        '''
        return len(self.meals_attended.all() | self.meals_signed_up.all())

    def is_full(self):
        '''
            Checks if the meal has filled the sophomore limit
        '''

        if self.num_of_sophomores() >= self.sophomore_limit:
            return True
        else:
            return False

    def sophomore_limit_text(self):
        '''
            Returns the display text
        '''

        return "%s/%s" % (self.num_of_sophomores(), self.sophomore_limit)



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
