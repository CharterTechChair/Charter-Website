import re, random, pdb

from django import forms
from django.shortcuts import redirect
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from events.models import Event, Room
from charterclub.models import Member
from datetime import date, timedelta, datetime


ROOMS = [ ("UDR", "UDR"), 
        ("Great Room", "Great Room"), 
        ("MDR", "MDR"),
        ("FJ", "FJ"),
        ("Stewart", "Stewart"),
        ("Library", "Library") ]


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['rooms']
        fields = ['event_choice', 'title', 'snippet', 'date_and_time',
                  'senior_signup_start', 'junior_signup_start',
                  'sophomore_signup_start', 'signup_end_time']
        
    event_choice = forms.ChoiceField()
    
    # title = forms.CharField(max_length = 255, initial="Charter's super awesome event")
    # description = forms.CharField(max_length = 10000, required = True, initial="This will be the most fun event ever ^_^")
    

    # Time fields describing relevant deadlines
    

    # Choose the rooms
    # chooserooms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('add', 'submit', css_class='btn-primary'))

    def __init__(self, *args, **kwargs):
        today = timezone.now()

        t1 = today + timedelta(days=1, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
        t2 = today + timedelta(days=2, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
        t3 = today + timedelta(days=3, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['event_choice'] = forms.ModelChoiceField(empty_label = "New Event",
                                   widget = forms.Select(attrs = {"onchange":"Dajaxice.events.loadevent(Dajax.process,{'event':this.value})"}),
                                   queryset = Event.objects.all())
        self.fields['chooserooms'] = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS, label = "Available Rooms", required = False)
        self.fields['date_and_time'] = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t3)
        self.fields['senior_signup_start']    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
        self.fields['junior_signup_start']    = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
        self.fields['sophomore_signup_start'] = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
        self.fields['signup_end_time'] = forms.DateTimeField(
                        help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t2)    
#        self.initial=Event.objects.get(pk=1)


    def clean(self):
        cleaned_data = super(EventCreateForm, self).clean()

        
        if not self.is_valid():
            return
        # Forbid events on the same day to have the same name
        title = cleaned_data.get('title')
        start = cleaned_data.get('date_and_time')
        end = start + timedelta(days=1)
        if not cleaned_data.get('event_choice') and Event.objects.filter(title=title, date_and_time__range=[start,end]):
            msg = "Events on the same date must have different times"
            msg += ". Current events:[ "
            msg += ",".join([str(e) for e in Event.objects.filter(date_and_time__range=[start,end])])
            msg += "]"

            raise forms.ValidationError(msg)

        # Signups must happen before the event goes up
        if cleaned_data.get('senior_signup_start') > cleaned_data.get('date_and_time'):
            raise forms.ValidationError('Senior sign up time cannot happen after the deadline for the event has started')
        if cleaned_data.get('junior_signup_start') > cleaned_data.get('date_and_time'):
            raise forms.ValidationError('Junior sign up time cannot happen after the deadline for the event has started')
        if cleaned_data.get('sophomore_signup_start') > cleaned_data.get('date_and_time'):
            raise forms.ValidationError('Sophomore sign up time cannot happen after the deadline for the event has started')

        # Signups must happen before the end deadline
        if cleaned_data.get('senior_signup_start') > cleaned_data.get('signup_end_time'):
            raise forms.ValidationError('Senior sign up time cannot happen after the deadline for the event signup')
        if cleaned_data.get('junior_signup_start') > cleaned_data.get('signup_end_time'):
            raise forms.ValidationError('Junior sign up time cannot happen after the deadline for the event signup')
        if cleaned_data.get('sophomore_signup_start') > cleaned_data.get('signup_end_time'):
            raise forms.ValidationError('Sophomore sign up time cannot happen after the deadline for the event signup')

        # Closure for signups must happen before the event occurs 
        if cleaned_data.get('signup_end_time') > cleaned_data.get('date_and_time'):
            raise forms.ValidationError('Ending signup time must happen before event happens')
        return

    def clean_title(self):
        ans = self.cleaned_data['title']
        # # restrict field to alphanumeric + whitespace
        # m = re.search(r'[\w\s0-9\']+', ans) 
        # if not m or m.group() != ans:
        #     raise forms.ValidationError("Title can not contain special characters like !,+*/ (etc)")
        return ans

    # Prevent events from being created in the past
    def clean_date_and_time(self):
        ans = self.cleaned_data['date_and_time']
        if ans < timezone.now():
            raise forms.ValidationError('Cannot create an event date in the past')
        return ans
    
    # Prevent sign up dates from being created in the past
    def clean_senior_signup_start(self):
        ans = self.cleaned_data['senior_signup_start']
        if ans < timezone.now():
            raise forms.ValidationError('Cannot create a signup date in the past')
        return ans

    def clean_junior_signup_start(self):
        ans = self.cleaned_data['junior_signup_start']
        if ans < timezone.now():
            raise forms.ValidationError('Cannot create a signup date in the past')
        return ans

    def clean_sophomore_signup_start(self):
        ans = self.cleaned_data['sophomore_signup_start']
        if ans < timezone.now():
            raise forms.ValidationError('Cannot create a signup date in the past')
        return ans

    def clean_signup_end_time(self):
        ans = self.cleaned_data['signup_end_time']
        print ans
        if ans < timezone.now():
            raise forms.ValidationError('Cannot create a signup end date in the past')
        return ans

    def save(self, commit = True, *args, **kwargs):
      
        instance = super(EventCreateForm, self).save(commit=False, *args, **kwargs)
        instance.pk = self.cleaned_data['event_choice'].pk
        rooms = self.cleaned_data['chooserooms']
        
        if not self.cleaned_data["event_choice"]:
            for r in rooms:
                room = Room(name=r, max_capacity=15)
                room.save()
                instance.rooms.add(room)

            self.cleaned_data['rooms'] = rooms

        print self.cleaned_data['signup_end_time']
        print instance.signup_end_time
        if commit:
            instance.save()

        
        return instance

    # obsolete! do not use this!
    def make_event(self):

        if self.is_valid():
            data = self.cleaned_data
            rooms = data['rooms']

            event = Event(pk=data['pk'],
                          title=data['title'], 
                          snippet=data['description'],
                          date_and_time=data['date_and_time'],
                          sophomore_signup_start=data['sophomore_signup_start'],
                          junior_signup_start=data['junior_signup_start'],
                          senior_signup_start=data['senior_signup_start'],
                          signup_end_time=data['signup_end_time'])

            event.save()

            for r in rooms:
              room = Room(name=r, max_capacity=15)
              room.save()
              event.rooms.add(room)
              event.save()
        else:
            raise Exception('EventCreateForm: Cannot make an event with invalid data')

class EventEditForm(forms.Form):
    event_choice = forms.ModelChoiceField(empty_label = "New Event",
                                          widget = forms.Select(attrs = {"onchange":"Dajaxice.events.loadevent(Dajax.process,{'event':this.value})"}),
                                          queryset = Event.objects.all())
    helper = FormHelper()



class EventChoiceForm(forms.Form):
    event_choice     = forms.ModelChoiceField(widget = forms.Select, queryset = Event.get_future_events())
    helper = FormHelper()   
    helper.add_input(Submit('add', 'submit', css_class='btn-primary'))


class EventEntryForm(forms.Form):
    # Fields that don't change from Event to Event
    guest_first_name = forms.CharField(max_length = 100, required = False, help_text="Leave blank if you do not plan on bringing a guest")
    guest_last_name = forms.CharField(max_length = 100, required = False, help_text="Leave blank if you do not plan on bringing a guest")

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    # Fields that do change from Event to Event
    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        self.netid = kwargs.pop('netid')
        super(EventEntryForm, self).__init__(*args, **kwargs)
        choices = [('yes', 'Yes, I will be coming to "%s"' % (self.event)), 
                   ('no', "Nope, I can't make it"                , )]
        self.fields['is_attending'] = forms.ChoiceField(choices=choices)
        self.fields['room_choice']= forms.ModelChoiceField(widget = forms.Select, queryset = self.event.rooms.all())
        
        for key in ['is_attending', 'guest_first_name', 'guest_last_name', 'room_choice']:
            self.fields[key] = self.fields.pop(key)
         


    def clean_room_choice(self):
        room = self.cleaned_data['room_choice']
        num_add = 0

        member = Member.objects.filter(netid=self.netid)[0]
        if not room.has_member(member):
            num_add += 1
        if self.cleaned_data['guest_first_name'] or self.cleaned_data['guest_last_name']:
            num_add += 1
        
        num_people = room.get_num_of_people()
        if (num_people + num_add > room.max_capacity):
            raise forms.ValidationError("Sorry! This room is beyond capacity (%s/%s) and cannot take %s more people" % (num_people, room.max_capacity, num_add))
        return room

