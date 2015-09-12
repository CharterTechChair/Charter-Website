import re, random, pdb
from copy import deepcopy

from collections import OrderedDict
from django import forms
from django.shortcuts import redirect
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from events.models import Event, Room, Entry

from charterclub.models import Member, Student
from datetime import date, timedelta, datetime



class EventEntryForm(forms.Form):
    '''
        A form that will create an event entry.
    '''

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    # Fields that do change from Event to Event
    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        self.student = kwargs.pop('student')


        super(EventEntryForm, self).__init__(*args, **kwargs)

        choices = [('yes', 'Yes, I will be coming to "%s"' % (self.event.title)), 
                   ('no', "No, I want to delete my rsvp from this event.")]

             
        self.fields['is_attending'] = forms.ChoiceField(label="Are you attending?", choices=choices)
        self.fields['room_choice']= forms.ModelChoiceField(required=True,
                                                          widget = forms.Select,
                                                          queryset = self.event.event_room.all(), )
        # Allow guest option if there is one
        if self.event.guest_limit != 0:
            self.fields['guest_first_name'] = forms.CharField(required=False, 
                                                              help_text="Leave blank if you're not bringing a guest")
            self.fields['guest_last_name'] = forms.CharField(required=False,
                                                              help_text="You can resubmit this form to bring more guests.")

    def clean(self):
        '''
            Check if there is space for the person to be in the room
        '''

        room = self.cleaned_data['room_choice']

        if self.cleaned_data['is_attending'] == 'no':
            raise forms.ValidationError("Use the 'delete' button at the top to remove your rsvp.")

        # Check the guest limit
        if self.cleaned_data['guest_first_name'] or self.cleaned_data['guest_last_name']:

            fname = self.cleaned_data.get('guest_first_name') or ''
            lname = self.cleaned_data.get('guest_last_name') or ''
            self.guest_name = ("%s %s" % (fname, lname)).strip()
            guests = self.event.get_guests(self.student)

            if len(guests) > self.event.guest_limit:
                raise forms.ValidationError("The guest limit is %s. You already have '%s' as your guests" % (self.event.guest_limit, guests))
        else:
            self.guest_name = ""

        
        # Check if there is another entry like it in the database
        query = self.event.entry_event_association.filter(room=room, student__netid=self.student.netid, guest=self.guest_name)

        if query:
            raise forms.ValidationError("We already got this submission. Check the 'Where people are sitting section'. Else, enter new data." )

        # Now check for overflow by putting the entry in
        entry = Entry(room=room, student=self.student, guest=self.guest_name, event=self.event)
        self.entry = entry
        entry.save()


        # Then check if the room has overflowed
        if room.num_people() > room.limit:
            entry.delete()
            raise forms.ValidationError("Sorry! %s cannot take more people (%s)" % (room, entry))
        
        # else, keep going
        entry.delete()


        return self.cleaned_data

    def execute_form_information(self):
        '''
            After form is valid, make the entry
        '''
        if self.is_valid():
            # Take care of room swaps
            query = self.event.entry_event_association.filter(student__netid=self.student.netid)
            if query:
                for q in query:
                    q.room = self.cleaned_data['room_choice']
                    q.save()
            
            # Check if there is something new to be added
            query = self.event.entry_event_association.filter(student__netid=self.student.netid, guest=self.guest_name)
            if not query:
                self.entry.save()


            # If we already ahve queries with guests, cleanup queries with members but no guests.
            query_withguest = self.event.entry_event_association.filter(student__netid=self.student.netid).exclude(guest='')
            query_noguest = self.event.entry_event_association.filter(student__netid=self.student.netid, guest='')

            if query_withguest:
                for q in query_noguest:
                    q.delete()




    

# class EventCreateForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         exclude = ['rooms']
#         fields = ['event_choice', 'title', 'snippet', 'date_and_time',
#                   'senior_signup_start', 'junior_signup_start',
#                   'sophomore_signup_start', 'signup_end_time']
        
#     event_choice = forms.ChoiceField()
    
#     # title = forms.CharField(max_length = 255, initial="Charter's super awesome event")
#     # description = forms.CharField(max_length = 10000, required = True, initial="This will be the most fun event ever ^_^")
    

#     # Time fields describing relevant deadlines
    

#     # Choose the rooms
#     # chooserooms = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS)

#     # Submit buttons
#     helper = FormHelper()   
#     helper.add_input(Submit('add', 'submit', css_class='btn-primary'))

#     def __init__(self, *args, **kwargs):
#         today = timezone.now()

#         t1 = today + timedelta(days=1, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
#         t2 = today + timedelta(days=2, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
#         t3 = today + timedelta(days=3, hours=random.randint(12,23), minutes=random.randint(0,59), seconds=random.randint(0,59)) 
#         super(EventCreateForm, self).__init__(*args, **kwargs)
        
#         self.fields['event_choice'] = forms.ModelChoiceField(empty_label = "New Event",
#                                    widget = forms.Select(attrs = {"onchange":"Dajaxice.events.loadevent(Dajax.process,{'event':this.value})"}),
#                                                              queryset = Event.objects.all(),
#                                                              required = False)
        
#         self.fields['chooserooms'] = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROOMS, label = "Available Rooms", required = False)
#         self.fields['date_and_time'] = forms.DateTimeField(
#                         help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t3)
#         self.fields['senior_signup_start']    = forms.DateTimeField(
#                         help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
#         self.fields['junior_signup_start']    = forms.DateTimeField(
#                         help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
#         self.fields['sophomore_signup_start'] = forms.DateTimeField(
#                         help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t1)
#         self.fields['signup_end_time'] = forms.DateTimeField(
#                         help_text="Enter date and time in the form '2006-10-25 14:30'", initial=t2)    
# #        self.initial=Event.objects.get(pk=1)


#     def clean(self):
#         cleaned_data = super(EventCreateForm, self).clean()

        
#         if not self.is_valid():
#             return
#         # Forbid events on the same day to have the same name
#         title = cleaned_data.get('title')
#         start = cleaned_data.get('date_and_time')
#         end = start + timedelta(days=1)
#         if not cleaned_data.get('event_choice') and Event.objects.filter(title=title, date_and_time__range=[start,end]):
#             msg = "Events on the same date must have different times"
#             msg += ". Current events:[ "
#             msg += ",".join([str(e) for e in Event.objects.filter(date_and_time__range=[start,end])])
#             msg += "]"

#             raise forms.ValidationError(msg)

#         # Signups must happen before the event goes up
#         if cleaned_data.get('senior_signup_start') > cleaned_data.get('date_and_time'):
#             raise forms.ValidationError('Senior sign up time cannot happen after the deadline for the event has started')
#         if cleaned_data.get('junior_signup_start') > cleaned_data.get('date_and_time'):
#             raise forms.ValidationError('Junior sign up time cannot happen after the deadline for the event has started')
#         if cleaned_data.get('sophomore_signup_start') > cleaned_data.get('date_and_time'):
#             raise forms.ValidationError('Sophomore sign up time cannot happen after the deadline for the event has started')

#         # Signups must happen before the end deadline
#         if cleaned_data.get('senior_signup_start') > cleaned_data.get('signup_end_time'):
#             raise forms.ValidationError('Senior sign up time cannot happen after the deadline for the event signup')
#         if cleaned_data.get('junior_signup_start') > cleaned_data.get('signup_end_time'):
#             raise forms.ValidationError('Junior sign up time cannot happen after the deadline for the event signup')
#         if cleaned_data.get('sophomore_signup_start') > cleaned_data.get('signup_end_time'):
#             raise forms.ValidationError('Sophomore sign up time cannot happen after the deadline for the event signup')

#         # Closure for signups must happen before the event occurs 
#         if cleaned_data.get('signup_end_time') > cleaned_data.get('date_and_time'):
#             raise forms.ValidationError('Ending signup time must happen before event happens')
#         return

#     def clean_title(self):
#         ans = self.cleaned_data['title']
#         # # restrict field to alphanumeric + whitespace
#         # m = re.search(r'[\w\s0-9\']+', ans) 
#         # if not m or m.group() != ans:
#         #     raise forms.ValidationError("Title can not contain special characters like !,+*/ (etc)")
#         return ans

#     # Prevent events from being created in the past
#     def clean_date_and_time(self):
#         ans = self.cleaned_data['date_and_time']
#         if ans < timezone.now():
#             raise forms.ValidationError('Cannot create an event date in the past')
#         return ans
    
#     # Prevent sign up dates from being created in the past
#     def clean_senior_signup_start(self):
#         ans = self.cleaned_data['senior_signup_start']
#         if ans < timezone.now():
#             raise forms.ValidationError('Cannot create a signup date in the past')
#         return ans

#     def clean_junior_signup_start(self):
#         ans = self.cleaned_data['junior_signup_start']
#         if ans < timezone.now():
#             raise forms.ValidationError('Cannot create a signup date in the past')
#         return ans

#     def clean_sophomore_signup_start(self):
#         ans = self.cleaned_data['sophomore_signup_start']
#         if ans < timezone.now():
#             raise forms.ValidationError('Cannot create a signup date in the past')
#         return ans

#     def clean_signup_end_time(self):
#         ans = self.cleaned_data['signup_end_time']
#         print ans
#         if ans < timezone.now():
#             raise forms.ValidationError('Cannot create a signup end date in the past')
#         return ans

#     def save(self, commit = True, *args, **kwargs):
      
#         instance = super(EventCreateForm, self).save(commit=False, *args, **kwargs)
#         if self.cleaned_data['event_choice']:
#             instance.pk = self.cleaned_data['event_choice'].pk
#         else:
#             instance.pk = None
        
#         rooms = self.cleaned_data['chooserooms']
        
#         if not self.cleaned_data["event_choice"]:
#             instance.save()
#             for r in rooms:
#                 room = Room(name=r, max_capacity=ROOM_CAPS[r])
#                 room.save()
#                 instance.rooms.add(room)

#             self.cleaned_data['rooms'] = rooms

#         print self.cleaned_data['signup_end_time']
#         print instance.signup_end_time
#         if commit:
#             instance.save()
        
#         return instance

#     # obsolete! do not use this!
#     def make_event(self):

#         if self.is_valid():
#             data = self.cleaned_data
#             rooms = data['rooms']

#             event = Event(pk=data['pk'],
#                           title=data['title'], 
#                           snippet=data['description'],
#                           date_and_time=data['date_and_time'],
#                           sophomore_signup_start=data['sophomore_signup_start'],
#                           junior_signup_start=data['junior_signup_start'],
#                           senior_signup_start=data['senior_signup_start'],
#                           signup_end_time=data['signup_end_time'])

#             event.save()

#             for r in rooms:
#               room = Room(name=r, max_capacity=15)
#               room.save()
#               event.rooms.add(room)
#               event.save()
#         else:
#             raise Exception('EventCreateForm: Cannot make an event with invalid data')

# class EventEditForm(forms.Form):
#     event_choice = forms.ModelChoiceField(empty_label = "New Event",
#                                           widget = forms.Select(attrs = {"onchange":"Dajaxice.events.loadevent(Dajax.process,{'event':this.value})"}),
#                                           queryset = Event.objects.all())
#     helper = FormHelper()



# class EventChoiceForm(forms.Form):
#     event_choice     = forms.ModelChoiceField(widget = forms.Select, queryset = Event.get_future_events())
#     helper = FormHelper()   
#     helper.add_input(Submit('add', 'submit', css_class='btn-primary'))


