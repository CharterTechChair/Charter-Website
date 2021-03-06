import re, random

from django import forms
from django.shortcuts import redirect
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from datetime import date, timedelta, datetime

from models import CalendarEvent

class AddCalendarEventForm(forms.Form):
   title = forms.CharField(max_length = 255)
   start = forms.DateTimeField(
                 help_text="Enter date and time in the form '2006-10-25 14:30'")
   end = forms.DateTimeField(
                 help_text="Enter date and time in the form '2006-10-25 14:30'")

   # Submit buttons
   helper = FormHelper()   
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

   def make_event(self):

      if self.is_valid():
         data = self.cleaned_data
         
         e = CalendarEvent(title=data['title'],
                           css_class='event-important',
                           start=data['start'],
                           end=data['end'])
         e.save()