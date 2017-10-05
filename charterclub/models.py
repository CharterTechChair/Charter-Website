from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType

import pdb
from collections import Counter

# from events.models import Event
from datetime import date, timedelta
from django.core.exceptions import ValidationError

# For analyzing Models
from django.db.models import Min, Max
from kitchen.models import Meal

from settings_charter.settings_service import DynamicSettingsServices

# Taken from: http://stackoverflow.com/questions/929029/how-do-i-access-the-child-classes-of-an-object-in-django-without-knowing-the-name/929982#929982
class InheritanceCastModel(models.Model):
    """
    An abstract base class that provides a ``real_type`` FK to ContentType.

    For use in trees of inherited models, to be able to downcast
    parent instances to their child types.

    """
    real_type = models.ForeignKey(ContentType, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(InheritanceCastModel, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)

    class Meta:
        abstract = True


###########################################################################
# a Person model
# Basically an Abstract class containing a person's name
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

class Person(InheritanceCastModel):
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
    order = models.IntegerField('Order of Appearance on Staff Page', blank=True)

    image = models.ImageField(upload_to = 'member_images/',
                              help_text='(optional)',
                              null=True,
                              blank=True,
                              validators=[validate_image])


###########################################################################
# Student model
# A Student of Princeton
############################################################################
class Student(Person):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z\.]*$', 'Only a mix of alphanumeric characters and peroids are allowed.')
    netid = models.CharField('Princeton Net ID', max_length=100, validators=[alphanumeric], unique=True)
    year = models.IntegerField('Graduation Year')

    class Meta:
            ordering = ("year", "last_name", "first_name",)

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

    def get_future_related_entries(self):
        from events.models import Entry
        return Entry.get_future_related_entries_for_student(self)

    def get_past_past_related_entries(self):
        from events.models import Entry

        return Entry.get_past_related_entries_for_student(self)

###########################################################################
# Prospective model
# A person who is thinking about joining Charter
############################################################################

def limit_meals_attended_choices():
    #June 3rd is the turnover date
    start_year = (timezone.now() - timedelta(days=153)).year

    start_date = "%s-08-11" % start_year
    end_date = "%s-08-11" % (start_year + 1)

    return {'day__range': [start_date, end_date]
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
    # events_attended = models.IntegerField(
    #     'Number of events attended', default=0)

    # meals_attended = models.ManyToManyField(Meal,
    #                 limit_choices_to=limit_meals_attended_choices,
    #                 blank=True, related_name="meals_attended")
    # meals_signed_up = models.ManyToManyField(Meal,
    #                 limit_choices_to=limit_meals_signed_up,
    #                 blank=True, related_name="meals_signed_up")

    mailing_list = models.BooleanField(default=True)

    # meals = make another model for meals signups? use date fields?
    def get_num_points(self):
        meal_points = sum([m.points for m in self.prospectivemealentry_set.all()])
        # event_points = sum([m.points for m in self.prospectiveevententry_set.all()])

        return meal_points #+ event_points

    # Promote a Prospective to a Member
    def promote_to_member(self, house_account):
        # fields = [f.get_attname() for f in Prospective._meta.fields]
        # bk_lst = ['id', 'events_attended', 'meals_attended', 'mailing_list']
        white_lst = ['netid', 'first_name', 'last_name', 'year']
        # fields = [f for f in fields if ('_id' not in f and f not in bk_lst)]

        # Create the parameters for an officer
        member_param = {f:getattr(self, f) for f in white_lst}
        member_param['house_account'] = house_account

        # self.delete() #Delete the old prospective
        self.delete()
        Member.objects.create(**member_param)



###########################################################################
# Member
# A Student of Princeton
############################################################################

def get_default_house_account():
    return DynamicSettingsServices.get('default_house_account_for_new_member')

def get_default_guest_meals():
    return DynamicSettingsServices.get('default_member_meals_per_semester')

# Member object begins here
class Member(Student):
    # ----- Fields associated with this Model ---
    house_account = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        default=get_default_house_account)
    guest_meals = models.IntegerField("number of guest meals this member has",
                                        default=get_default_guest_meals)
    image = models.ImageField(upload_to = 'member_images/',
                              help_text='(optional)',
                              null=True,
                              blank=True,
                              validators=[validate_image])
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
            #TODO: YOLO
            Member.objects.update(**member_param)
#            raise Exception('Creation Error: Member with netid "%s" already exists' % param['netid'])
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

        self.delete()
        # Now re-insert as an officer
        Officer.objects.create(**officer_param)


    # Get the years in which membership spans over
    @staticmethod
    def get_membership_years():
        years = []

        minn = Member.objects.exclude(netid='charter').order_by('year')[0].year
        maxx = Member.objects.exclude(netid='charter').order_by('-year')[1].year

        return range(minn, maxx)


    def __iter__(self):
        for m in self.all():
            yield m

import events.models

class Officer(Member):
    position = models.CharField('Position/title', max_length=100)
    is_active = models.BooleanField('Current Officer', default=True, max_length=100)
    order = models.IntegerField('Order of Appearance on Officer Page', blank=True)

    class Meta:
        ordering = ("is_active", "year", "order", "last_name", "first_name",)

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

