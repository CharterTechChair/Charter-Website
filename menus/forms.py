from django import forms
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from menus.models import MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['date', 'lunch_food', 'dinner_food']
        
#    day = forms.ChoiceField(widget=forms.Select, choices=DAYS)
#     date = forms.DateField(widget=forms.DateInput,
#                         help_text="Enter date in the form '10/25/2006'")
#    lunch = forms.TextArea()
#    dinner = forms.CharField(max_length=None,
#                help_text="input newlines with '&#60;br&#62;'")

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        dates = [today + datetime.timedelta(days=i) for i in range(0,14)]
        choices = []

        # allow entry for days in the next two weeks
        for d in dates:
            if d.weekday() == 6 and not d == dates[0]:
                choices.append((None, "----------"))

            # format as month day, day-of-week
            choices.append( (d, d.strftime("%b %d, %A")) )

        self.fields['date'] = forms.ChoiceField(widget=forms.Select,
                                                choices = choices,
                                                initial = choices[0])
    
    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))
