from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)

from functools import partial

##################################################
#   MealSignup Form
#   Allows sophomores to sign up for meals
###################################################

class MealSignupForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }), help_text="Choose a date")
    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def add_soph(self):
        print "hello world from add_soph"