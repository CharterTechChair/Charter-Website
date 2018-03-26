from django import forms

# Cripsy forms makes forms look nicer
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class FeedbackForm(forms.Form):
   helper = FormHelper()
   subject = forms.CharField(label="Subject", required=True)
   anonymous_feedback  = forms.CharField(
      widget=forms.Textarea, 
      label="Anonymous Feedback",
      required=True)
   response = forms.BooleanField(
      label="Get a response",
      help_text="Check this box if you want a response on the response page.",
      initial=False,
      required=False,
    )
   cc_myself = forms.BooleanField(
        label="CC Myself",
        help_text="Check this box if you want to include yourself in the thread. Otherwise, your submission will be anonymous.",
        initial=False,
        required=False,
    )
   helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))
