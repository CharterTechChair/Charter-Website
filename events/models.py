from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms

from charterclub.models import *

# -- Models for Events ---
class Room(models.Model):
    name = models.CharField(max_length=40)

    max_capacity = models.IntegerField(
        'Max capacity for that room for a specific event')
    members = models.ManyToManyField(Member)
    guests  = models.ManyToManyField(Guest) # Guests can be members or non-members

    def __unicode__(self):
        return "%s (%s/%s)" % (self.name, self.get_num_of_people(), self.max_capacity)

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

    # Add to a room, avoiding duplicates
    def add_pair_to_room(self, member, guest):
        if not member:
            raise Exception("Error: must need to add at least one member to the room")

        # Stops adding to the room twice
        if not self.get_listing(member):
            self.members.add(member)
        if guest and not self.get_listing(guest):
            guest.member_association = member
            guest.save()
            self.guests.add(guest)
            
        
    # returns the room that the person is in
    def get_listing(self, person):
        if not person:
            return None

        for m in self.members.all():
            if m.first_name == person.first_name and m.last_name == person.last_name:
                return self.members
        for g in self.guests.all():
            if g.first_name == person.first_name and g.last_name == person.last_name:
                return self.guests
        return None

    def get_person(self, person):
        if not person:
            return None

        for m in self.members.all():
            if m.first_name == person.first_name and m.last_name == person.last_name:
                return m
        for g in self.guests.all():
            if g.first_name == person.first_name and g.last_name == person.last_name:
                return g
        return None

    # safely remove the person from the room
    def remove_from_room(self, person):
        listing = self.get_listing(person)
        casted_person = self.get_person(person)

        # Remove the person
        if casted_person:
            listing.remove(casted_person)
        else:
            raise Exception("Error, person '%s' was not found in Member and Guest List" % person)


        # If the listing was the members listing, remove the guest
        if type(listing) == type(self.members):
            guest = self.get_guest_of_member(person)
            if guest:
                self.guests.remove(guest)

    def get_guest_of_member(self, member):
        lookup = self.guests.filter(member_association=member)
        if not lookup:
            return None
        return lookup[0]

    class Meta:
        ordering = ("name",)

class Event(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)

    # Some times
    date_and_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    # Times for Junior Seniors and Sophomores
    sophomore_signup_start = models.DateTimeField(blank=True)
    junior_signup_start    = models.DateTimeField(blank=True)
    senior_signup_start    = models.DateTimeField(blank=True)
    

    rooms = models.ManyToManyField(Room)

    # Add a pairing to this event
    def add_to_event(self, member, guest, room):
        room_m = self.get_room_of_person(member)
        room_g = self.get_room_of_person(guest)

        # If member and th
        if room_m:
            room_m.remove_from_room(member)
        if room_g:
            room_g.remove_from_room(guest)


        room.add_pair_to_room(member, guest)

    # Remove a person or guest from this event
    def remove_from_event(self, person):
        if not person:
            return
        # If removing a member, also remove the guest
        if type(person) == Member:
            room_m = self.get_room_of_person(person)
            guest = room_m.get_guest_of_member(person)
            room_m.remove_from_room(person)

            if guest:
                room_m.remove_from_room(guest)
        # If removing a guest
        elif type(person) == Guest:
            room_g = self.get_room_of_person()
            room_g.remove_from_room(guest)
        else:
            raise Exception("Invalid Type '%s' for function remove_from_event(self, person)" % type(person))

    # Get the room of the person
    def get_room_of_person(self, person):
        if not person:
            return None

        for r in self.rooms.all():
            if r.get_listing(person):
                return r
        return None

    def to_JSON(self):
        data = {}
        data['title'] = self.title
        data['snippet'] = self.snippet
        data['date_and_time'] = self.date_and_time
        data['rooms'] = []

        for r in self.rooms.all():
            data['rooms'].append(r.to_JSON())

        return data

    def get_future_events():
        startdate = date.today() - timedelta(days=1)
        enddate = startdate + timedelta(weeks=52)
        elist = Event.objects.filter(date_and_time__range=[startdate, enddate])

        return elist

    def __unicode__(self):
        return "%s, %s" % (self.title, self.date_and_time.isoformat()[:10])

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
class MenuItem(models.Model):
    day = models.CharField(choices=DAYS, max_length=10)
#     date = models.DateField()
    lunch_food = models.CharField(max_length=1000)
    dinner_food = models.CharField(max_length=1000)
