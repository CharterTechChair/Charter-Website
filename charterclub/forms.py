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

class WinetastingForm(forms.Form):
   helper2 = FormHelper()
   first_name = forms.CharField(max_length = 100)
   last_name = forms.CharField(max_length = 100)
   has_guest = forms.BooleanField(required = False)
   guest_first_name = forms.CharField(max_length = 100, required = False)
   guest_last_name = forms.CharField(max_length = 100, required = False)
   helper2.add_input(Submit('submit', 'submit', css_class='btn-primary'))