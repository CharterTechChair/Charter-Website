from django.contrib import admin
from sophomore_meals.models import Meal

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meal Information',          {'fields': ['day', 'meals', 'allow_sophomore']}),
        ('Meal Display Information', {'fields': ['description', 'grill', 'plated_option', 'salad']}),
        ('Other',                    {'fields': ['special_note']}),
    ]


    list_display = ['__unicode__', 'allow_sophomore', 'description', 'special_note']
    list_editable = ['allow_sophomore', ]
    # list_editable = ['allow_sophomore', 'description_s', 'special_note']

admin.site.register(Meal, MealAdmin)
