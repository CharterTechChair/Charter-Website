from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from datetime import date, timedelta

from models import *

from charterclub.models import Prospective

DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]

################################################################################
# MemberListForm
# 
# For Django Admin in URL: /admin/charterclub/member/add-members/
# 
# MemberListForm is a special form that will allow a list of members
#       to be added to the database.
################################################################################
class MemberListForm(forms.Form):
    placeholder = '''Quan, Zhou, quanzhou, 2015, 255.00
    Rory, Fitzpatrick, roryf, 2016, 255.00
    Jeremy, Whitton, jwhitton, 2016, 0.00
    '''.replace('    ','')
    content = forms.CharField(label='content', 
                        max_length=2000,
                        widget=forms.Textarea(attrs={
                        'style' : 'height:480px',
                        'placeholder': placeholder}))
    # Submit buttons
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit'))

    ## ---- User defined Methods -----
    # Check if content has proper character seperated values
    def clean(self):
        data = self.cleaned_data['content'].strip()
        table = []

        for row in data.split("\n"):
            table.append([l.strip() for l in row.strip().split(',')])

        line_s = [l.strip() for l in data.split('\n')]

        # Check that every row can be split into 4 colums
        for (i,row) in enumerate(table):
            if not len(row) == 5:
                raise ValidationError('Something is wrong with the following line:\n"%s"' % line_s[i])        
            if not any(row):
                raise ValidationError('Comma Error: Empty column in %s' % line_s[i])        
            if not (row[2].isalnum()):
                raise ValidationError('"%s" is not a valid netid' % line_s[2])

        self.table = table
        self.cleaned_data['content'] = "\n".join([",".join(r) for r in table])
        return self.cleaned_data

    # Tries to parse itself. 
    # If successful, returns the results [was prospective, new member, existing member]
    # If unsuccessful, raises an error
    def parse_content(self):
        results = {}
        self.clean()

        # Now try to do lookup for students
        for row in self.table:
            netid = row[2]

            pquery_o = Prospective.objects.filter(netid=netid)
            mquery_o = Member.objects.filter(netid=netid)


            if mquery_o:
                results[netid] = ('"%s" already exists in Member database.' 
                                % (mquery_o[0].__unicode__()),0, row)
            elif pquery_o:
                results[netid] = ('Was a prospective. Points: %s.'  
                                % (pquery_o[0].get_num_points()), 1,row)
            else:
                results[netid] = ('Adding brand a new member.', 2, row)

        return results

    # Makes the entries - requires the form to be filled out first
    def submit_content(self):
        result_list = self.parse_content()
        # Based on what the person is, do actions
        for netid, tup in result_list.iteritems():
            info = tup[2]
            mquery_o = Member.objects.filter(netid=netid)
            pquery_o = Prospective.objects.filter(netid=netid)

            if mquery_o:
                pass
            elif pquery_o: 
                pquery_o[0].promote_to_member(info[4])
            else:
                m = Member(first_name=info[0], last_name=info[1], netid=netid,
                       year=info[3], house_account=info[4], allow_rsvp=True)
                m.save()

################################################################################
# NewOfficerForm
# form to create a new officer: take an existing member and turn
# them into an officer, adding their title
################################################################################
class NewOfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['position', 'order']
        
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
        fields = ['order']

year = (date.today() + timedelta(days=6*30)).year
years = [year, year+1, year+2, year+3]

YEARS = []

for y in years:
    YEARS.append((y, str(y)))

