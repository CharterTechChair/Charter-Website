from django.contrib import admin
from django import forms

from charterclub.models import Prospective
from charterclub.models import limit_meals_attended_choices
from recruitment.models import ProspectiveMealEntry#, ProspectiveEventEntry
from kitchen.models import Meal


class ProspectiveMealEntryInline(admin.TabularInline):
    model = ProspectiveMealEntry
    extra = 1

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     '''
    #         Limit the meals to the ones that would have happened this year. 
    #     '''

    #     field = super(ProspectiveMealEntryInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #     if db_field.name in ['meal']:
    #         if request._obj_ is not None:
    #             search_param = limit_meals_attended_choices() # From charterclub.models.limit_meals_attended_choices
    #             field.queryset = field.queryset.filter(event=request._obj_) 
    #         else:
    #             field.queryset = field.queryset.none()
    #     return field

# class ProspectiveEventEntryInline(admin.TabularInline):
#     model = ProspectiveEventEntry
#     extra = 1

#     readonly_fields=['Form_Answers', 'Event_Name', 'Room_Name',]
#     exclude=('answers','event', 'room')


#     def Form_Answers(self, obj):
#         return "\n".join([ans.__unicode__() for ans in obj.answers.all()])

#     def Event_Name(self, obj):
#         return self.event.__unicode__()

#     def Room_Name(self, obj):
#         return self.room.__unicode__()
