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

