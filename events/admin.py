from django.contrib import admin
from events.models import Event, Room

class RoomAdmin(admin.ModelAdmin):
    pass
class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', 
                                { 'fields': ['title', 'snippet', 'date_and_time']}),
        ('Signup Information', 
                                { 'fields': ['signup_end_time',
                                            'senior_signup_start',
                                            'junior_signup_start',
                                            'sophomore_signup_start']}),
        ('Rooms',
                                {'fields' : ['rooms']})
    ]

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
