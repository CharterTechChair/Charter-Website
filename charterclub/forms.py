from django import forms
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from charterclub.models import Event
from datetime import date, timedelta


ROOMS = [("UDR", "UDR"), ("Great Room", "Great Room"), ("MDR", "MDR"), ("FJ", "FJ")]

class FeedbackForm(forms.Form):
   helper = FormHelper()
   anonymous_feedback  = forms.CharField(
      widget=forms.Textarea, 
      label="Anonymous Feedback",
      required=False)
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))



class EventEntryForm(forms.Form):
    # Events that are available
    startdate = date.today() - timedelta(days=1)
    enddate = startdate + timedelta(weeks=52)
    elist = Event.objects.filter(date_and_time__range=[startdate, enddate])
    event = forms.ModelChoiceField(queryset=elist)
    
    
    # Questios
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    has_guest = forms.BooleanField(required = False)
    guest_first_name = forms.CharField(max_length = 100, required = False)
    guest_last_name = forms.CharField(max_length = 100, required = False)
    room_choice   = forms.ChoiceField(widget = forms.Select, choices = ROOMS)
    
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







