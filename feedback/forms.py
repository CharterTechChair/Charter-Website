from django import forms

# Cripsy forms makes forms look nicer
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class FeedbackForm(forms.Form):
   helper = FormHelper()
   anonymous_feedback  = forms.CharField(
      widget=forms.Textarea, 
      label="Anonymous Feedback",
      required=False)
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))



