from django.contrib import admin
from events.models import Event, Room, Entry

# class RoomAdmin(admin.ModelAdmin):
#     pass
class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

class EntryInline(admin.TabularInline):
    description = "hello"
    model = Entry
    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Mininum Information', 
                                { 'fields': ['title', 'snippet', 'date', 'time', 'image',],
                                  'description' : "Instructions: Fill the 'Mininum Information' and 'Room' fields. The rest of this form contain optional fields."}),
        ('Extra Event Fields', 
                                {'description' : "You can change these if you'd like.",
                                'fields' : ['guest_limit', 'is_points_event', 'prospective_limit']}),
        ('Signup Information', 
                                {'description' : 'More optional parameters.',
                                 'fields': ['senior_signup_start',
                                            'junior_signup_start',
                                            'sophomore_signup_start',
                                            'prospective_signup_start',
                                            'signup_end_time']}),
        # ('Rooms',
        #                         {'fields' : ['rooms']})
    ]

    inlines = [RoomInline, EntryInline]
    list_display = ['__unicode__', 'snippet', 'is_points_event', 'prospective_limit']
    ordering = ['-date']


# # Register your models here.
admin.site.register(Event, EventAdmin)
# admin.site.register(Room, RoomAdmin)
