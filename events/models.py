import urllib, datetime
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from  django.core.urlresolvers import reverse

from charterclub.models import Member

# Defines a relationship from a room to member
class Seating(models.Model):
    member = models.ForeignKey('charterclub.Member')
    guest  = models.CharField(max_length=255, blank=True) 

    def __unicode__(self):
        return "<%s, %s>" % (self.member, self.guest)

    class Meta:
        ordering = ("member",)

# Defines an instance of a room with a name, max capacity, members, and their relationships
class Room(models.Model):
    name = models.CharField(max_length=255)

    max_capacity = models.IntegerField('Max capacity for that room for a specific event')
    seatings     = models.ManyToManyField(Seating) # Unique by member

    def __unicode__(self):
        return "%s (%s/%s)" % (self.name, self.get_num_of_people(), self.max_capacity)

    # Returns whether the member exists in this room
    def has_member(self, member):
        search = self.seatings.filter(member=member)
        if search:
            return True
        else:
            return False

    # Returns whether a guest exists in this room
    def has_guest(self, guest):
        search = self.seatings.filter(member=member)
        if search:
            return True
        else:
            return False

    # Add a member (instance) and a guest (string) to the room
    def add_pair_to_room(self, member, guest_s):
        if self.has_member(member):
            raise Exception("Cannot add the same member to the room twice.")

        seating_n = Seating(member=member, guest=guest_s)
        seating_n.save()
        self.seatings.add(seating_n)

    # Removes a member and their guest from this room
    def remove_member(self, member):
        if not self.has_member(member):
            raise Exception("Member does not exist in this room")
        seating = self.get_seating(member)

        self.seatings.remove(seating)

    # Gets the number of people in this room
    def get_num_of_people(self):
        ans = 0
        for seating in self.seatings.all():
            if seating.guest != '':
                ans += 2
            else:
                ans += 1
        return ans

    # Returns the guest of the member
    def get_guest_of_member(self, member):
        if not self.has_member(member):
            raise Exception("Error: Member does not exist in this room")
        return self.seatings.filter(member=member)[0].guest


    # Get seating based off fo the member entry
    def get_seating(self, member):
        search = self.seatings.filter(member=member)
        if not search:
            return None
        if len(search) != 1:
            raise Exception('Member "%s" has multiple seatings' % search)
        return search[0]

    # Converts this into a JSON Object
    def to_JSON(self):
        return {
            'name'          : self.name, 
            'max_capacity'  : self.max_capacity,
            'people'        : [(str(s.member), str(s.guest)) for s in self.seatings.all()],
            'total'         : self.get_num_of_people()
        }

    class Meta:
        ordering = ("name",)

# An event contains instances of rooms
class Event(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=10000, blank=True)

    # Some times
    date_and_time   = models.DateTimeField()
    signup_end_time = models.DateTimeField()

    # Times for Junior Seniors and Sophomores
    sophomore_signup_start = models.DateTimeField()
    junior_signup_start    = models.DateTimeField()
    senior_signup_start    = models.DateTimeField()

    rooms = models.ManyToManyField(Room)

    # Get the room of the person
    def get_room_of_member(self, member):
        if not member:
            return None

        for r in self.rooms.all():
            if r.get_seating(member):
                return r
        return None
    # Has the person
    def has_member(self, member):
        if self.get_room_of_member(member):
            return True
        else:
            return False

    # Adds the person to this event, prohibits adding the same person twice
    def add_to_event(self, member, guest_s, room):
        # If this member is in a different room
        if self.get_room_of_member(member):
            r = self.get_room_of_member(member)
            s = r.get_seating(member)
            r.remove_member(member)    

        room.add_pair_to_room(member, guest_s)

    # Remove a person or guest from this event
    def remove_from_event(self, member):
        room = self.get_room_of_member(member)
        if not room:
            raise Exception('Cannot find Member "%s" in Event "%s"' % (member, self))
        room.remove_member(member)

    def to_JSON(self):
        data = {}
        data['title'] = self.title
        data['snippet'] = self.snippet
        data['date_and_time'] = self.date_and_time
        data['rooms'] = []

        for r in self.rooms.all():
            data['rooms'].append(r.to_JSON())

        return data

    def get_signup_url(self):
        url =  'events/signup'
        url += "/%s/%s" % (self.title, self.date_and_time.isoformat()[:10])
        return urllib.quote(url)


    def get_unrsvp_url(self):
        url =  'events/unrsvp'
        url += "/%s/%s" % (self.title, self.date_and_time.isoformat()[:10])
        return urllib.quote(url)

    def get_view_url(self):
        url =  'events/view'
        url += "/%s/%s" % (self.title, self.date_and_time.isoformat()[:10])
        return urllib.quote(url)
    
    @staticmethod   
    def get_future_events():
        startdate = timezone.now() - datetime.timedelta(days=1)
        enddate = startdate + datetime.timedelta(weeks=52)
        elist = Event.objects.filter(date_and_time__range=[startdate, enddate])

        return elist

    def __unicode__(self):
        return "%s, %s" % (self.title, self.date_and_time.isoformat()[:10])
    
    class Meta:
        ordering = ("title",)

