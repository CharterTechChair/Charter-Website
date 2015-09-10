from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
from django.core.validators import RegexValidator

import pdb
from collections import Counter

# from events.models import Event
from datetime import date, timedelta
from django.core.exceptions import ValidationError

# For analyzing Models
from django.db.models import Min, Max

from kitchen.models import Meal



###########################################################################
# a Person model
# Basically an Abstract class containing a person's name
############################################################################
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class meta:
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
#     picture_path = models.CharField(
#         'Relative path from /static/img/faceboard/',
#         max_length=200, blank=True)
  
###########################################################################
# Staff model
# Inherits from person
############################################################################  
class Staff(Person):
    position = models.CharField('Staff\'s position/title', max_length=100)
    
###########################################################################
# Student model
# A Student of Princeton
############################################################################
class Student(Person):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    netid = models.CharField('Princeton Net ID', max_length=100, validators=[alphanumeric])
    year = models.IntegerField('Graduation Year')

    # Calculate the senior year
    @staticmethod
    def get_senior_year():
        return (timezone.now() - timedelta(days=153)).year + 1
    # def __init__(self, member):
    #     self.pk = member.pk
    #     self.netid = member.netid
    #     self.year = member.year
    #     self.first_name = member.first_name
    #     self.last_name = member.last_name


###########################################################################
# Prospective model
# A person who is thinking about joining Charter
############################################################################  

def limit_meals_attended_choices():
    #June 3rd is the turnover date
    start_year = (timezone.now() - timedelta(days=153)).year

    start_date = "%s-08-11" % start_year
    end_date = "%s-08-11" % (start_year + 1)

    return {'sophomore_limit__gt': 0,
            'day__range': [start_date, end_date]
    }

def limit_meals_signed_up():
    #June 3rd is the turnover date
    start_year = (timezone.now() - timedelta(days=153)).year

    start_date = "%s-08-11" % start_year
    end_date = "%s-08-11" % (start_year + 1)

    return {'sophomore_limit__gt': 0,
            'day__range': [start_date, end_date]
    }


class Prospective(Student):
    events_attended = models.IntegerField(
        'Number of events attended')
    meals_attended = models.ManyToManyField(Meal, 
                    limit_choices_to=limit_meals_attended_choices,
                    blank=True, related_name="meals_attended")
    meals_signed_up = models.ManyToManyField(Meal, 
                    limit_choices_to=limit_meals_signed_up,
                    blank=True, related_name="meals_signed_up")

    monthly_meal_limit = 3

    # meals = make another model for meals signups? use date fields?
    def get_num_points(self):
        return self.events_attended

    # Get upcoming meals
    def get_upcoming_meals(self):
        return self.meals_signed_up.filter(day__gte=timezone.now())

    # Promote a Prospective to a Member
    def promote_to_member(self, house_account):
        fields = [f.get_attname() for f in Prospective._meta.fields]
        bk_lst = ['id', 'events_attended', 'meals_attended']
        fields = [f for f in fields if ('_id' not in f and f not in bk_lst)]

        # Create the parameters for an officer
        member_param = {f:getattr(self, f) for f in fields}
        member_param['house_account'] = house_account

        
        # self.delete() #Keep the old Prospective
        Member.objects.create(**member_param)

    #CHECK if montly meal limit has been exceeded
    def will_exceed_meal_limit(self, next_meal):
        total_meals = self.meals_attended.all() | self.meals_signed_up.all()
        group =  ["%s-%s" % (m.day.month, m.day.year) for m in total_meals]

        group.append("%s-%s" % (next_meal.day.month, next_meal.day.year))

        freq = Counter(group)
        print freq
        if  any(f > Prospective.monthly_meal_limit for f in freq.itervalues()):
            return True        

###########################################################################
# Member
# A Student of Princeton
############################################################################
# Make sure that the image is not too big
def validate_image(fieldfile_obj):
    # Note: this function is put up here so that validators=[func] can 
    #       be called on it
    filesize = fieldfile_obj.file.size
    kilobyte_limit = 50
    if filesize > kilobyte_limit*1024:
        raise ValidationError("Max file size is %sKB. Sorry! This is to ensure that\
         the site doesn't freeze when faceboard photos are loaded." % str(kilobyte_limit))

# Member object begins here
class Member(Student):
    # ----- Fields associated with this Model ---
    house_account = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to = 'member_images/', null=True, blank=True, validators=[validate_image])
    allow_rsvp = models.BooleanField(
        'Whether or not this member may attend events', default=True)

    # Get the events associated with the member
    def get_events(self):
        ans = []

        # Do a brute force search through all of the events, the rooms, and the seatings
        for e in events.models.Event.objects.all():
            for r in e.rooms.all():
                for member, guest_s in r.get_people_as_objects():
                    
                    if member == self:
                        ans.append((e, r, guest_s))
        return ans

    # Creates a member, if possible
    def create_new_member(self, param):
        if Members.objects.filter(netid=param['netid']):
            raise Exception('Creation Error: Member with netid "%s" already exists' % param['netid'])
        else:
            Member.objects.create(**member_param)

    # Promote the current member to an officer position
    def promote_to_officer(self, position, order=99):
        # Get the fields of the Student class
        fields = [f.get_attname() for f in Member._meta.fields]
        fields = [f for f in fields if ('_id' not in f and f !='id')]

        # Create the parameters for an officer
        officer_param = {f:getattr(self, f) for f in fields}
        officer_param['position'] = position
        officer_param['is_active'] = True
        officer_param['order'] = order

        # Now re-insert as an officer
        Officer.objects.create(**officer_param)
        self.delete()

    # Get the years in which membership spans over
    @staticmethod
    def get_membership_years():
        years = []
        minn = Member.objects.all().aggregate(Min('year'))['year__min']
        maxx = Member.objects.all().aggregate(Max('year'))['year__max']

        for y in range(minn, maxx+1):
            if Member.objects.filter(year=y):
                years.append(y)
                
        return years


    def __iter__(self):
        for m in self.all():
            yield m

import events.models

class Officer(Member):
    position = models.CharField('Position/title', max_length=100)
    is_active = models.BooleanField('Current Officer', default=True, max_length=100)
    order = models.IntegerField('Order of Appearance on Officer Page', max_length=100)

# THIS WILL GET MOVED TO A CAL APP EVENTUALLY
class SocialEvent(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)

    # Some times
    date_and_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]

