from django.contrib import admin
from kitchen.models import Meal, Brunch, Lunch, Dinner
from recruitment.prospective_admin_inline import ProspectiveMealEntryInline

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    fieldsets = [
        ('Meal Information',          {'fields': ['name', 'day', 'sophomore_limit']}),
        ('Meal Display Information', {'fields': ['description',]}),
        ('Other',                    {'fields': ['special_note', 'optional_pdf']}),
    ]


    list_display = ['cast_unicode', 'name', 'sophs', 'sophomore_limit', 'description', 'special_note']
    list_editable = ['sophomore_limit', ]
    ordering = ['-day']

    inlines = [ProspectiveMealEntryInline]

    def cast_unicode(self, obj):
        return obj.cast().__unicode__()

    def sophs(self, obj):
        return obj.num_of_sophomores()
    
# admin.site.register(Meal, MealAdmin)
class BrunchAdmin(MealAdmin):
    pass
admin.site.register(Brunch, BrunchAdmin)


class LunchAdmin(MealAdmin):
    pass

admin.site.register(Lunch, LunchAdmin)


class DinnerAdmin(MealAdmin):
    pass
admin.site.register(Dinner, DinnerAdmin)



