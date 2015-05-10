from django.db import models

# A menu for a single day
class MenuItem(models.Model):
    class Meta:
        ordering = ['date']
#    day = models.CharField(choices=DAYS, max_length=10)
    date = models.DateField()
    lunch_food = models.TextField()
    dinner_food = models.TextField()
