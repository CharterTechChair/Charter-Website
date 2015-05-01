from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

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
    netid = models.CharField('Person\'s Princeton Net ID', max_length=100)
    year = models.IntegerField('Person\'s Graduation Year')


class Prospective(Student):
    events_attended = models.IntegerField(
        'Number of events this prospective has attended')
    # meals = make another model for meals signups? use date fields?
    
class Guest(Student):
    member_association = models.ForeignKey('Member')

class Member(Student):
    allow_rsvp = models.BooleanField(
        'Whether or not this member may attend events', default=True)
    house_account = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    

class Officer(Member):
    position = models.CharField('Officer\'s position/title', max_length=100)

# -- Models for Events ---
class Room(models.Model):
    name = models.CharField(max_length=40)
    max_capacity = models.IntegerField(
        'Max capacity for that room for a specific event')
    members = models.ManyToManyField(Member)
    guests  = models.ManyToManyField(Guest)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name",)
class Event(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    date_and_time = models.DateTimeField(blank=True)

    rooms = models.ManyToManyField(Room)

