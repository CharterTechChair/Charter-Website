import urllib, datetime, json
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from  django.core.urlresolvers import reverse
from django import forms

from charterclub.models import Member, Student

from datetime import time
now = timezone.now()

def JSON_validator(arg):
    try:
        json.loads(arg)
    except:
        return False
    return True

# Defines a relationship from a room to member
class Entry(models.Model):
    member = models.ForeignKey('charterclub.Member', 
            limit_choices_to={'year__gte' : Student.get_senior_year(), 
                              'year__lte' : Student.get_senior_year() + 2})
    guests  = models.CharField(default="[]",
                            max_length=1000,
                            blank=True,
                            validators=[JSON_validator])

    room = models.ForeignKey('Room', related_name="entry_association")
    event = models.ForeignKey('Event', related_name="entry_association")

    def __unicode__(self):
        return "<%s, %s>" % (self.member, self.guest)

    class Meta:
        ordering = ("member",)

class Room(models.Model):
    name = models.CharField(max_length=255, help_text="Where is the Event Held?")
    limit = models.IntegerField()
    event = models.ForeignKey('Event')

    def __unicode__(self):
        return "%s, %s/%s" % (self.name, len(self.entry_association.all()), self.limit)


# # Defines an instance of a room with a name, max capacity, members, and their relationships
# class Room(models.Model):
#     name = models.CharField(max_length=255)
#     max_capacity = models.IntegerField('Max capacity for that room for a specific event')
#     seatings     = models.ManyToManyField(Seating) # Unique by member

#     # event = models.ManyToManyField(Event) # point back

#     def __unicode__(self):
#         return "%s (%s/%s)" % (self.name, self.get_num_of_people(), self.max_capacity)

#     # Returns whether the member exists in this room
#     def has_member(self, member):
#         search = self.seatings.filter(member=member)
#         if search:
#             return True
#         else:
#             return False

#     # Returns whether a guest exists in this room
#     def has_guest(self, guest):
#         search = self.seatings.filter(member=member)
#         if search:
#             return True
#         else:
#             return False

#     # Add a member (instance) and a guest (string) to the room
#     def add_pair_to_room(self, member, guest_s):
#         if self.has_member(member):
#             raise Exception("Cannot add the same member to the room twice.")

#         seating_n = Seating(member=member, guest=guest_s)
#         seating_n.save()
#         self.seatings.add(seating_n)

#     # Removes a member and their guest from this room
#     def remove_member(self, member):
#         if not self.has_member(member):
#             raise Exception("Member does not exist in this room")
#         seating = self.get_seating(member)

#         self.seatings.remove(seating)

#     # Gets the number of people in this room
#     def get_num_of_people(self):
#         ans = 0
#         for seating in self.seatings.all():
#             if seating.guest != '':
#                 ans += 2
#             else:
#                 ans += 1
#         return ans

#     # Returns the guest of the member
#     def get_guest_of_member(self, member):
#         if not self.has_member(member):
#             raise Exception("Error: Member does not exist in this room")
#         return self.seatings.filter(member=member)[0].guest


#     # Get seating based off fo the member entry
#     def get_seating(self, member):
#         search = self.seatings.filter(member=member)
#         if not search:
#             return None
#         if len(search) != 1:
#             raise Exception('Member "%s" has multiple seatings' % search)
#         return search[0]

#     # Converts this into a JSON Object
#     def to_JSON(self):
#         return {
#             'name'          : self.name, 
#             'max_capacity'  : self.max_capacity,
#             'people'        : self.get_people_as_string(),
#             'total'         : self.get_num_of_people()
#         }

#     def get_people_as_string(self):
#         return [(str(s.member), str(s.guest)) for s in self.seatings.all()]
    
#     def get_people_as_objects(self):
#         return [(s.member, str(s.guest)) for s in self.seatings.all()]  

#     class Meta:
#         ordering = ("name",)

# An event contains instances of rooms
DEFAULT_TIME = time(hour=17, minute=0, second=0)
class Event(models.Model):
    title = models.CharField("Title",
                            help_text="Name of the Event", 
                            max_length=255)
    snippet = models.TextField("Description", 
                                help_text="To be displayed on the website. (Optional).",
                                blank=True)
    image   =  models.ImageField(help_text="To be displayed on the website. (Optional).",
                                upload_to = 'event_images/', 
                                 null=True, 
                                 blank=True,
                                 )
    is_points_event = models.BooleanField("Is Point Event:", 
                                           help_text="Do Prospectives who attend get points?",
                                           default=False)

    prospective_limit = models.IntegerField("Prospectives Limit", 
                                            help_text="set 0 to not allow prospectives",
                                            default=0)

    guest_limit = models.IntegerField("Guest Limit", 
                                      help_text="0 = No guests allowed. -1 = As many guests as they can.",
                                      default=1)
    # Event time Some times
    date   = models.DateField("Date of Event", default=now)
    time = models.TimeField("Time of Event", help_text="IMPORTANT. THIS IS IN MILITARY TIME.", 
                            default=DEFAULT_TIME)

    signup_end_time = models.DateField(default=now)

    # Times for Junior Seniors and Sophomores
    prospective_signup_start = models.DateField(default=now, blank=True)
    sophomore_signup_start = models.DateField(default=now, blank=True)
    junior_signup_start    = models.DateField(default=now, blank=True)
    senior_signup_start    = models.DateField(default=now, blank=True)

    # Filled with rooms
    # rooms = models.ManyToManyField('Room', related_name="event_to_room_assignment")

    # # Get the room of the person
    # def get_room_of_member(self, member):
    #     if not member:
    #         return None

    #     for r in self.rooms.all():
    #         if r.get_seating(member):
    #             return r
    #     return None
    # # Has the person
    # def has_member(self, member):
    #     if self.get_room_of_member(member):
    #         return True
    #     else:
    #         return False

    # # Adds the person to this event, prohibits adding the same person twice
    # def add_to_event(self, member, guest_s, room):
    #     # If this member is in a different room
    #     if self.get_room_of_member(member):
    #         r = self.get_room_of_member(member)
    #         s = r.get_seating(member)
    #         r.remove_member(member)    

    #     room.add_pair_to_room(member, guest_s)

    # # Remove a person or guest from this event
    # def remove_from_event(self, member):
    #     room = self.get_room_of_member(member)
    #     if not room:
    #         raise Exception('Cannot find Member "%s" in Event "%s"' % (member, self))
    #     room.remove_member(member)

    # def to_JSON(self):
    #     data = {}
    #     data['title'] = self.title
    #     data['snippet'] = self.snippet
    #     data['date'] = self.date
    #     data['rooms'] = []

    #     for r in self.rooms.all():
    #         data['rooms'].append(r.to_JSON())

    #     return data

    # def get_signup_url(self):
    #     url =  'events/signup'
    #     url += "/%s/%s" % (self.title, self.date.isoformat()[:10])
    #     return urllib.quote(url)


    # def get_unrsvp_url(self):
    #     url =  'events/unrsvp'
    #     url += "/%s/%s" % (self.title, self.date.isoformat()[:10])
    #     return urllib.quote(url)

    # def get_view_url(self):
    #     url =  'events/view'
    #     url += "/%s/%s" % (self.title, self.date.isoformat()[:10])
    #     return urllib.quote(url)
    
    # @staticmethod   
    # def get_future_events():
    #     startdate = timezone.now() - datetime.timedelta(days=1)
    #     enddate = startdate + datetime.timedelta(weeks=52)
    #     elist = Event.objects.filter(date__range=[startdate, enddate])

        # return elist

    def __unicode__(self):
        return "%s, %s" % (self.title, self.date.isoformat()[:10])
    
    class Meta:
        ordering = ("title",)

