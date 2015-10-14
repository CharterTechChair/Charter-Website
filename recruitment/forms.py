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
    year = forms.IntegerField(help_text='Your Graduation Year', required=True)

        # Fields that do change from Event to Event
    def __init__(self, *args, **kwargs):
        self.netid = kwargs.pop('netid')
        super(AccountCreationForm, self).__init__(*args, **kwargs)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))

    def clean(self):
        # returns none if tigerbooks fails
        info = tigerbooks_lookup(self.netid)
        
        # Use tigerbooks API to pull data
        if info:
            info['year'] = info['class_year']
            del info['class_year']
            info['netid'] = self.netid
        # If no data, use  a custom sign-in info
        else:
            info = {}
            info['first_name'] = self.cleaned_data['first_name']
            info['last_name'] = self.cleaned_data['last_name']
            info['netid'] = self.netid
            info['year'] = self.cleaned_data['year']

        info['year'] = 2018
        # Check for errors
        if info['year'] < Student.get_senior_year() + 2:
            raise forms.ValidationError('The Class of %s can join directly. Please contact our President/Vice-President to get more details.' % info['year'])
        if info['year'] > Student.get_senior_year() + 2:
            raise forms.ValidationError('You must be a sophomore to create a prospective account. Upperclassman can join directly.')
        query = Prospective.objects.filter(netid=info['netid'])
        if query:
            raise forms.ValidationError('Oops. Looks like you already made an account with us. To login, click "login" from the dropdown in the top right corner.')
      
        self.prospective = Prospective(**info)
    

    def create_account(self):
        if self.is_valid():
            self.prospective.save()
            return self.prospective


# ################################################################################
# # MailingListForm
# # To add sophomores based on the mailing list
# ################################################################################
# class MailingListForm(forms.Form):
#     # Fields of this Form
    
#     netid = forms.CharField(max_length=10)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     year = forms.ChoiceField(widget=forms.Select, choices=YEARS)

#     # Submit buttons
#     helper = FormHelper()   
#     helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

#     # Add sophomores based on the data collected
#     def add_soph(self):
#         if self.is_valid():
#             data = self.cleaned_data
            
#             p = Prospective.objects.filter(netid=data['netid'])
#             if not p:
#                 pnew = Prospective(netid=data['netid'],
#                                    first_name=data['first_name'],
#                                    last_name=data['last_name'],
#                                    year=data['year'],
#                                    events_attended=0)
#                 pnew.save()

        

    # def __init__(self, *args, **kwargs):
    #     super(MemberListForm, self).__init__(*args, **kwargs)
    #     self.helper.form_tag = False

