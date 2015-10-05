from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)

from functools import partial

from kitchen.models import Brunch, Lunch, Dinner
from charterclub.models import Prospective

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
        self.clean()
        prospective.meals_signed_up.add(self.meal)


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

        print self.prospective

        # Now check if the meal is full
        if m[0].is_full():
            raise ValidationError('Sorry! This meal has been filled up. Try refreshing the data.')
        if self.prospective.will_exceed_meal_limit(m[0]):
            raise ValidationError('You\'ve reached the limit of %s meals per month' % Prospective.monthly_meal_limit)
        
        self.meal = m[0]

        return self.cleaned_data
