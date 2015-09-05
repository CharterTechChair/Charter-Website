from django.contrib import admin
from kitchen.models import Meal, Brunch, Lunch, Dinner

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    fieldsets = [
        ('Meal Information',          {'fields': ['name', 'day', 'sophomore_limit']}),
        ('Meal Display Information', {'fields': ['description',]}),
        ('Other',                    {'fields': ['special_note']}),
    ]


    list_display = ['__unicode__', 'name', 'sophomore_limit', 'description', 'special_note']
    list_editable = ['sophomore_limit', ]
    ordering = ['-day']


class BrunchAdmin(MealAdmin):
    pass
admin.site.register(Brunch, BrunchAdmin)


class LunchAdmin(MealAdmin):
    pass

admin.site.register(Lunch, LunchAdmin)


class DinnerAdmin(MealAdmin):
    pass
admin.site.register(Dinner, DinnerAdmin)



