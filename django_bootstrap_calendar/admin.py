from django.contrib import admin
import forms
from django_bootstrap_calendar.models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    fields = ['title', 'start', 'end']

admin.site.register(CalendarEvent, CalendarEventAdmin)
