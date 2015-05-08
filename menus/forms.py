from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]

class MenuForm(forms.Form):
    day = forms.ChoiceField(widget=forms.Select, choices=DAYS)
#     date = forms.DateField(widget=forms.DateInput,
#                         help_text="Enter date in the form '10/25/2006'")
    lunch = forms.CharField(max_length=None,
                help_text="input newlines with '&#60;br&#62;'")
    dinner = forms.CharField(max_length=None,
                help_text="input newlines with '&#60;br&#62;'")

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))