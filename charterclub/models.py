from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
from django.core.validators import RegexValidator
# from events.models import Event

    
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
    
class Staff(Person):
    position = models.CharField('Staff\'s position/title', max_length=100)
    
class Student(Person):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    netid = models.CharField('Princeton Net ID', max_length=100, validators=[alphanumeric])
    year = models.IntegerField('Graduation Year')

    # def __init__(self, member):
    #     self.pk = member.pk
    #     self.netid = member.netid
    #     self.year = member.year
    #     self.first_name = member.first_name
    #     self.last_name = member.last_name

class Prospective(Student):
    events_attended = models.IntegerField(
        'Number of events attended')
    # meals = make another model for meals signups? use date fields?
    
class Guest(Person):
    member_association = models.ForeignKey('Member')

class Member(Student):
    allow_rsvp = models.BooleanField(
        'Whether or not this member may attend events', default=True)
    house_account = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def get_events(self):
        ans = []
        print self

        for e in events.models.Event.objects.all():
            print e
            for r in e.rooms.all():
                for member in r.get_people():
                    if member[0] == self:
                        ans.append((e, r))
                    if len(member) > 1:
                        if member[1] == self:
                            ans.append((e, r))
        return ans

    def __iter__(self):
        for m in self.all():
            yield m

import events.models

class Officer(Member):
    position = models.CharField('Position/title', max_length=100)

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

