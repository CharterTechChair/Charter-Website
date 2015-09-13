from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)

from functools import partial

from kitchen.models import Brunch, Lunch, Dinner
from charterclub.models import Prospective, Student

from charterclub.permissions import tigerbooks_lookup

##################################################
#   Account Creation Form
#   Allows sophomores to create their account
#################################################

class AccountCreationForm(forms.Form):
    first_name = forms.CharField(help_text='',
                                 required=True,
                                 )
    last_name = forms.CharField(help_text='',
                                required=True,
                                 )
    netid = forms.CharField(help_text="We'll use our API to look you up.",
                            required=True,)
    year = forms.IntegerField(help_text='Your Graduation Year', required=True)


    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def clean_netid(self):
        return self.cleaned_data['netid'].strip().lower()

    def clean(self):
        info = tigerbooks_lookup(self.cleaned_data['netid'])
   
        # Use tigerbooks API to pull data
        if info:
            info['year'] = info['class_year']
            del info['class_year']
            info['netid'] = self.cleaned_data['netid']
        # If no data, use  a custom sign-in info
        else:
            info = {}
            info['first_name'] = self.cleaned_data['first_name']
            info['last_name'] = self.cleaned_data['last_name']
            info['netid'] = self.cleaned_data['netid']
            info['year'] = self.cleaned_data['year']

        # Check for errors
        if info['year'] < Student.get_senior_year() + 2:
            raise forms.ValidationError('Upperclassman can join directly. You should contact our President/Vice-President to get more details.')
        if info['year'] > Student.get_senior_year() + 2:
            raise forms.ValidationError('You must be a sophomore to create a prospective account. Upperclassman can join directly.')
        query = Prospective.objects.filter(netid=info['netid'])
        if query:
            raise forms.ValidationError('Oops. Looks like you already made an account with us. To login, click "login" from the dropdown in the top right corner.')

        info['events_attended'] = 0
        
        self.prospective = Prospective(**info)
    

    def create_account(self):
        if self.is_valid():
            self.prospective.save()
            return self.prospective


