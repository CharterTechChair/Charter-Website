from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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
    
class Member(Student):
    allow_rsvp = models.BooleanField(
        'Whether or not this member may attend events', default=True)
    house_account = models.DecimalField(max_digits=10, decimal_places=2)

class Officer(Member):
    position = models.CharField('Officer\'s position/title', max_length=100)

class Event(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    date_and_time = models.DateTimeField(blank=True)

class Series(Event):
    series_id = models.IntegerField('Series ID')

class winetastingRoom(models.Model):
    room = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=100)