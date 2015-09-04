from django.contrib import admin
from kitchen.models import Meal

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meal Information',          {'fields': ['name', 'day', 'meals', 'sophomore_limit']}),
        ('Meal Display Information', {'fields': ['description', 'grill', 'plated_option', 'salad']}),
        ('Other',                    {'fields': ['special_note']}),
    ]


    list_display = ['__unicode__', 'name', 'sophomore_limit', 'description', 'special_note']
    list_editable = ['sophomore_limit', ]
    ordering = ['-day']
    # list_editable = ['sophomore_limit', 'description_s', 'special_note']

admin.site.register(Meal, MealAdmin)
