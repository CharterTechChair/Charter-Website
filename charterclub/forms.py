from django import forms
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class FeedbackForm(forms.Form):
   helper = FormHelper()
   anonymous_feedback  = forms.CharField(
      widget=forms.Textarea, 
      label="Anonymous Feedback",
      required=False)
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

ROOMS = [   ("Main Dining Room", "Main Dining Room"),
            ("Great Room", "Great Room"),
            ("Upstairs Dining Room", "Upstairs Dining Room"),
            ("Ferguson-Jacobs Room", "Ferguson-Jacobs Room")]
class WinetastingForm(forms.Form):
   helper = FormHelper()
   first_name        = forms.CharField(max_length=50)
   last_name         = forms.CharField(max_length=50)
   guest             = forms.BooleanField()
   guest_first_name  = forms.CharField(max_length=50, required=False)
   guest_last_name   = forms.CharField(max_length=50, required=False)
   room   = forms.ChoiceField(widget = forms.Select, choices = ROOMS)
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))