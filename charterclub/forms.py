from django import forms
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from datetime import date, timedelta

from models import *
from ldap_student_lookup import get_student_info

DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]


# form for entering a new member into the database
# takes a netid as input as uses ldap lookup to find corresponding
# first name, last name, and graduation year.
class NewMemberForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['netid', 'allow_rsvp', 'house_account']

    def save(self, commit=True):
        newMember = super(NewMemberForm, self).save(commit = False)
        
        student = get_student_info(newMember.netid)
        newMember.first_name = student.first_name
        newMember.last_name = student.last_name
        newMember.year = student.year
        
        if commit:
            newMember.save()

        return newMember


# form to create a new officer: take an existing member and turn
# them into an officer, adding their title
class NewOfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['position']
        
    member_choice = forms.ModelChoiceField(widget = forms.Select, queryset = Member.objects.all())             

    def save(self, commit=True):
        newOfficer = super(NewOfficerForm, self).save(commit = False)
        member_choice = self.cleaned_data.get("member_choice", None)
        newOfficer.first_name = member_choice.first_name
        newOfficer.last_name = member_choice.last_name
        newOfficer.netid = member_choice.netid
        newOfficer.year = member_choice.year
        newOfficer.house_account = member_choice.house_account
        newOfficer.allow_rsvp = member_choice.allow_rsvp

        if commit:
            newOfficer.save()
        
        return newOfficer

class EditOfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['position']

year = (date.today() + timedelta(days=6*30)).year
years = [year, year+1, year+2, year+3]

YEARS = []

for y in years:
    YEARS.append((y, str(y)))

class MailingListForm(forms.Form):
    netid = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    year = forms.ChoiceField(widget=forms.Select, choices=YEARS)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def add_soph(self):

        if self.is_valid():
            data = self.cleaned_data
            
            p = Prospective.objects.filter(netid=data['netid'])
            print "here"
            if not p:
                pnew = Prospective(netid=data['netid'],
                                   first_name=data['first_name'],
                                   last_name=data['last_name'],
                                   year=data['year'],
                                   events_attended=0)
                pnew.save()

