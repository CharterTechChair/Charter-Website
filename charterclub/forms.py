from django import forms
from django.forms.extras.widgets import SelectDateWidget

class FeedbackForm(forms.Form):
  # anon_feedback        = forms.CharField(max_length=1000)
   anonymous_feedback        = forms.CharField(widget=forms.Textarea)

  # last_name         = forms.CharField(max_length=50)