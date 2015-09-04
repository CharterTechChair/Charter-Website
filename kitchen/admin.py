from django.contrib import admin
from kitchen.models import Meal

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meal Information',          {'fields': ['name', 'day', 'meals', 'allow_sophomore']}),
        ('Meal Display Information', {'fields': ['description', 'grill', 'plated_option', 'salad']}),
        ('Other',                    {'fields': ['special_note']}),
    ]


    list_display = ['__unicode__', 'name', 'allow_sophomore', 'description', 'special_note']
    list_editable = ['name', 'allow_sophomore', ]
    ordering = ['-day']
    # list_editable = ['allow_sophomore', 'description_s', 'special_note']

admin.site.register(Meal, MealAdmin)
