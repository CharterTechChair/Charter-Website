from django.db import models

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance." % model.__name__)

# Create your models here.
class CharterClubSettings(models.Model):
    default_sophomore_meal_per_month = models.PositiveIntegerField("sophomore meal cap per month", default=2)
    default_member_meals_per_semester = models.PositiveIntegerField("default number of guest meals for new member account", 
                                                                    default=4)
    default_house_account_for_new_member = models.DecimalField( 
                                    max_digits=10, decimal_places=2,
                                    default=255.00)
    #todo: might want to include a default_active_sophomore_limit_on_meal
    def clean(self):
        validate_only_one_instance(self)

    def __unicode__(self):
        return "Default settings"