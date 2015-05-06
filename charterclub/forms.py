from django import forms
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from charterclub.models import Event
from datetime import date, timedelta


ROOMS = [ ("UDR", "UDR"), 
        ("Great Room", "Great Room"), 
        ("MDR", "MDR"),
        ("FJ", "FJ"),
        ("Stewart", "Stewart"),
        ("Library", "Library") ]

class FeedbackForm(forms.Form):
   helper = FormHelper()
   anonymous_feedback  = forms.CharField(
      widget=forms.Textarea, 
      label="Anonymous Feedback",
      required=False)
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class EventCreateForm(forms.Form):
    title = forms.CharField(max_length = 40)
    snippet = forms.CharField(max_length = 150, required = False)
    date_and_time = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    # end_time = forms.DateTimeField(required = False)
    sophomore_signup_start = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    junior_signup_start    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")
    senior_signup_start    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'")

    rooms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('add', 'submit', css_class='btn-primary'))

class EventEntryForm(forms.Form):
    # Events that are available
    # event = forms.ModelChoiceField(queryset=Event.get_future_events())
    event = Event.objects.filter(title='Formals')[0]
    
    
    # Questios
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    has_guest = forms.BooleanField(required = False)
    guest_first_name = forms.CharField(max_length = 100, required = False)
    guest_last_name = forms.CharField(max_length = 100, required = False)
    room_choice     = forms.ModelChoiceField(widget = forms.Select, queryset = event.rooms.all())
    
    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def clean_room(self):
        room_choice_s = self.cleaned_data['room_choice']
        event  = self.cleaned_data['event']

        room = event.rooms.filter(name=room_choice_s)[0]

        add_people = 1 + int(self.cleaned_data['has_guest'] == 'true')

        if (room.get_num_of_people() + add_people > room.max_capacity):
            raise forms.ValidationError("Sorry! This room is beyond capacity")
        return room_choice_s