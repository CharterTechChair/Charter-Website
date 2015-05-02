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
    
class Guest(Person):
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

    def to_JSON(self):
        data = {}
        data['name'] = self.name
        data['max_capacity'] = self.max_capacity
        data['people'] = self.get_people()
        data['total'] = self.get_num_of_people()

        return data

    def get_people(self):
        ans = []
        for m in self.members.all():
            lookup = self.guests.filter(member_association=m)

            if lookup: 
                ans.append((m, lookup[0]))
            else:
                ans.append((m, ))
        return ans

    def get_num_of_people(self):
        ans = 0
        for m in self.members.all():
            lookup = self.guests.filter(member_association=m)

            if lookup: 
                ans += 2
            else:
                ans += 1
        return ans
    
    class Meta:
        ordering = ("name",)

class Event(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    date_and_time = models.DateTimeField(blank=True)

    rooms = models.ManyToManyField(Room)

    def to_JSON(self):
        data = {}
        data['title'] = self.title
        data['snippet'] = self.snippet
        data['date_and_time'] = self.date_and_time
        data['rooms'] = []

        for r in self.rooms.all():
            data['rooms'].append(r.to_JSON())

        return data

    def __unicode__(self):
        return "%s, %s" % (self.title, self.date_and_time.isoformat()[:10])

