import re

from django import forms
from django.shortcuts import redirect
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from events.models import Event
from datetime import date, timedelta

ROOMS = [ ("UDR", "UDR"), 
        ("Great Room", "Great Room"), 
        ("MDR", "MDR"),
        ("FJ", "FJ"),
        ("Stewart", "Stewart"),
        ("Library", "Library") ]



class EventCreateForm(forms.Form):
    title = forms.CharField(max_length = 40)
    description = forms.CharField(max_length = 150, required = False)
    date_and_time = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    # end_time = forms.DateTimeField(required = False)
    senior_signup_start    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    junior_signup_start    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    sophomore_signup_start = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    

    rooms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('add', 'submit', css_class='btn-primary'))

    
    def clean_title(self):
        ans = self.cleaned_data['title']
        # restrict field to alphanumeric + whitespace
        m = re.search(r'[\w\s0-9]+', ans) 
        if m or m.group() == ans:
            raise forms.ValidationError("Title can not contain special characters like !,+*/ (etc)")

        # forbid events on the same day to have the same name
        start =  self.cleaned_data['date_and_time'].date()
        end = start + datetime.timedelta(days=1)
        if Event.objects.filter(title=ans, date_and_time__range=[start,end]):
            raise forms.ValidationError("Events on the same date must have different times")

        return ans


class EventChoiceForm(forms.Form):
    event_choice     = forms.ModelChoiceField(widget = forms.Select, queryset = Event.get_future_events())
    helper = FormHelper()   
    helper.add_input(Submit('add', 'submit', css_class='btn-primary'))


class EventEntryForm(forms.Form):
    # Fields that don't change from Event to Event
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    guest_first_name = forms.CharField(max_length = 100, required = False)
    guest_last_name = forms.CharField(max_length = 100, required = False)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    # Fields that do change from Event to Event
    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        super(EventEntryForm, self).__init__(*args, **kwargs)
        
        self.fields['room_choice']= forms.ModelChoiceField(widget = forms.Select, queryset = self.event.rooms.all())
        
    def clean_room(self):
        room = self.cleaned_data['room_choice']
        
        num_add = 0

        member_s = Member.objects.filter(first_name=self.cleaned_data['first_name'], 
                                         last_name=self.cleaned_data['last_name'])

        guest_s = Guest.objects.filter(first_name=self.cleaned_data['guest_first_name'], 
                                       last_name=self.cleaned_data['guest_last_name'])

        if not member_s or room.has_person(member_s[0]):
            num_add += 1
        if not guest_s or room.has_person(guest[0]):
            num_add += 1
        
        if (room.get_num_of_people() + num_add > room.max_capacity):
            raise forms.ValidationError("Sorry! This room is beyond capacity")
        return room

class AddSocialEventForm(forms.Form):
    title = forms.CharField(max_length = 40)
    snippet = forms.CharField(max_length = 150, required = False)
    date_and_time = forms.DateTimeField(
                    help_text="Enter date and time in the form '2006-10-25 14:30'")
    end_time = forms.DateTimeField(
                    help_text="Enter date and time in the form '2006-10-25 14:30'")

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

