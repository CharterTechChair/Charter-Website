from django import forms
from django.forms.extras.widgets import SelectDateWidget

class FeedbackForm(forms.Form):
   anonymous_feedback  = forms.CharField(widget=forms.Textarea)