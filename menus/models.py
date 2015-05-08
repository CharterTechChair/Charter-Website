from django.db import models


DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]
        
# Create your models here.
class MenuItem(models.Model):
    day = models.CharField(choices=DAYS, max_length=10)
#     date = models.DateField()
    lunch_food = models.CharField(max_length=1000)
    dinner_food = models.CharField(max_length=1000)
