from collections import Counter

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.shortcuts import redirect

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)

from functools import partial

from kitchen.models import Brunch, Lunch, Dinner
from charterclub.models import Prospective

from recruitment.models import ProspectiveMealEntry

from settings_charter.settings_service import DynamicSettingsServices
##################################################
#   MealSignup Form
#   Allows sophomores to sign up for meals
###################################################
class MealSignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.prospective = kwargs.pop('prospective')
        return super(MealSignupForm, self).__init__(*args, **kwargs)

    date = forms.DateField(help_text="Choose a date", required=True,
                           widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    meal_type = forms.ChoiceField(required=True, help_text="Choose one type of meal", 
                                choices = (('Brunch', 'Brunch'),
                                           ('Lunch',  'Lunch'),
                                           ('Dinner', 'Dinner')))
                                # widget=forms.Select(attrs={'class':'meal-type-field'}))

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def add_prospective(self, prospective):
        if self.is_valid():
            entry = ProspectiveMealEntry(meal=self.meal, prospective=self.prospective)
            entry.save()


    def clean(self):
        date = self.cleaned_data['date']
        meal_type = self.cleaned_data['meal_type']

        # Do the query
        if meal_type == 'Brunch':
            m = Brunch.objects.filter(day=date)
        elif meal_type == 'Lunch':
            m = Lunch.objects.filter(day=date)
        elif meal_type == 'Dinner':
            m = Dinner.objects.filter(day=date)
        else:
            raise ValidationError('Not Appropriate MealType:%s' % meal_type)

        # Check if there is a meal on that date
        if not m:
            raise ValidationError('There is not a meal of type:%s on date %s' % (meal_type, date))

        limit = DynamicSettingsServices.get('default_sophomore_meal_per_month')
        # Now check if the meal is full
        if m[0].is_full():
            raise ValidationError('Sorry! This meal has been filled up. Try refreshing the data.')
        if will_exceed_meal_limit(self.prospective, m[0]):
            raise ValidationError('You\'ve reached the limit of %s meals per month' % limit)
        if already_signed_up_for_meal(self.prospective, m[0]):
            raise ValidationError("Looks like you've already signed up for this meal %s" % m[0])
        self.meal = m[0]

        return self.cleaned_data

    #CHECK if montly meal limit has been exceeded
def will_exceed_meal_limit(prospective, next_meal):
    this_months_entries = prospective.prospectivemealentry_set.filter(meal__day__month=timezone.now().date().month)
    group =  ["%s-%s" % (entry.meal.day.month, entry.meal.day.year) for entry in this_months_entries]

    group.append("%s-%s" % (next_meal.day.month, next_meal.day.year))

    freq = Counter(group)
    print freq

    limit = DynamicSettingsServices.get('default_sophomore_meal_per_month')
    if  any(f > limit for f in freq.itervalues()):
            return True        

def already_signed_up_for_meal(prospective, meal):
    if prospective.prospectivemealentry_set.filter(meal=meal):
        return True
    return False
        
##################################################
#   MealSignup Form
#   Allows sophomores to cancel a meal on a specific date
###################################################
class MealCancellationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.meal_entry = kwargs.pop('meal_entry')
 
        super(MealCancellationForm, self).__init__(*args, **kwargs)
    
        self.fields['affirmation'] = forms.ChoiceField(label="Delete %s?" % self.meal_entry.meal,
                                        required= True,
                                        choices= (('Yes', 'Yes'),
                                                  ('No', 'No')))

    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    def clean_affirmation(self):
        data = self.cleaned_data['affirmation']
        if not data == 'Yes':
            raise forms.ValidationError('You must select "Yes" to delete this meal')
        return data

    def delete_meal(self):
        if self.cleaned_data['affirmation'] == 'Yes':
            self.meal_entry.delete()
            

