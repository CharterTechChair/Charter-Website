import urllib, datetime,  re
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


class Question(models.Model):
    question_text = models.CharField("Question Text", 
                                max_length=1e3)
    help_text = models.CharField("Help Text", blank=True,
                                max_length=1e3)
    event = models.ForeignKey('Event')
    required = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.event, self.question_text)

class Answer(models.Model):
    question = models.ForeignKey('Question', related_name="question_answer_association")
    answer_text =  models.CharField("Answer", 
                                max_length=1e3)

    def __unicode__(self):
        return "%s:%s" % (self.question.question_text, self.answer_text)

class Entry(models.Model):
    '''
        Defines one person's entry into an event.
    '''
    student = models.ForeignKey('charterclub.Student', 
            limit_choices_to={'year__gte' : Student.get_senior_year(), 
                              'year__lte' : Student.get_senior_year() + 2,},
                              related_name='event_student_association',
                              related_query_name="student",)
    guest  = models.CharField(max_length=1000, blank=True,)

    event = models.ForeignKey('Event', related_name="entry_event_association")
    room = models.ForeignKey('Room', related_name="entry_room_association")

    # Answers to any questions
    answers = models.ManyToManyField("Answer")

    class Meta:
            ordering = ("event", "room", "student",)

    def __unicode__(self):
        if self.guest:
            return "%s: %s %s with guest %s in %s" % (self.student.cast().__class__.__name__, 
                                                      self.student.first_name,
                                                      self.student.last_name,
                                                      self.guest,
                                                      self.room.__unicode__())
        else:
            return "%s: %s %s in %s" % (self.student.cast().__class__.__name__, 
                                                      self.student.first_name,
                                                      self.student.last_name,
                                                      self.room.__unicode__())
    def get_deletion_url(self):
        return urllib.quote('events/delete/' + self.__unicode__().replace("/","|") + "/" + str(self.id))
    
    def get_change_answers_url(self):
        return urllib.quote('events/change/' + self.__unicode__().replace("/","|") + "/" + str(self.id))

    def get_guest_change_url(self):
        return urllib.quote('events/guest_change/' + self.__unicode__().replace("/","|") + "/" + str(self.id))

    def get_room_change_url(self):
        return urllib.quote('events/room_change/' + self.__unicode__().replace("/","|") + "/" + str(self.id))

class Room(models.Model):
    '''
        A Room to an event.
    '''
    name = models.CharField(max_length=255, help_text="Where is the Event Held?")
    limit = models.IntegerField()
    event = models.ForeignKey('Event', related_name="event_room")
    
    class Meta:
            ordering = ("event", "name", "limit",)

    def __unicode__(self):
        return "%s %s/%s" % (self.name, self.num_people(), self.limit)

    def num_people(self):
        '''
            This method of counting unique names technically does break if 
            two people have the same name,but that is very rare.
        '''

        ans = 0

        for entry in self.entry_room_association.all():

            if entry.guest:
                ans += 2
            else:
                ans += 1
        return ans

        # names = set()
        # # Count the unique names
        # for entry in self.entry_room_association.all():
        #     s = entry.student
        #     s_name = "%s %s" % (s.first_name, s.last_name)
        #     g_name = entry.guest
            
        #     # clean the names
        #     s_name_c = re.sub(r'\W+^\s', '', s_name).lower().strip()
        #     g_name_c = re.sub(r'\W+^\s', '', g_name).lower().strip()

        #     if s_name_c:
        #         names.add(s_name_c)
        #     if g_name_c:
        #         names.add(g_name_c)

        # return len(names)
        
    def which_entries(self, student):
        '''
            Get all the entries that this person is a part of.
        '''

        entry_q = self.entry_room_association.filter(student__netid=student.netid)
        guest_q = self.entry_room_association.filter(guest__icontains=student.first_name)\
                                              .filter(guest__icontains=student.last_name)
        return entry_q | guest_q

# An event contains instances of rooms
DEFAULT_TIME = time(hour=17, minute=0, second=0)
# Make sure that the image is not too big
def validate_image(fieldfile_obj):
    # Note: this function is put up here so that validators=[func] can 
    #       be called on it
    filesize = fieldfile_obj.file.size
    kilobyte_limit = 1024
    if filesize > kilobyte_limit*1024:
        raise ValidationError("Max file size is %sKB. If the filesize is too big, the page will be very slow to laod for people with bad connections." % str(kilobyte_limit))


class Event(models.Model):
    '''
        An event to which people can RSVP.
    '''
    title = models.CharField("Title",
                            help_text="Name of the Event", 
                            max_length=255)
    snippet = models.TextField("Description", 
                                help_text="To be displayed on the website. (Optional).",)
    image   =  models.ImageField(help_text="To be displayed on the website. (Optional).",
                                upload_to = 'event_images/', 
                                 null=True, 
                                 blank=True,
                                 validators=[validate_image],
                                 )
    is_points_event = models.BooleanField("Is Point Event:", 
                                           help_text="Do Prospectives who attend get points?",
                                           default=False)

    prospective_limit = models.IntegerField("Prospectives Limit", 
                                            help_text="set 0 to not allow prospectives. This will also hide it on the website from them (email me, Quan, to turn this feature off).",
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
    signup_time            = models.TimeField("Start/End  Time for signups", help_text="IMPORTANT. THIS IS IN MILITARY TIME.", 
                            default=DEFAULT_TIME)    

    # Room is done with an ForeignKey

    class Meta:
            ordering = ("date", "time", "name",)
            
    def get_signup_url(self):
        '''
            return the url for signup
        '''
        url =  'events/signup'
        url += "/%s/%s" % (self.title, self.id)
        return urllib.quote(url)

    def get_officer_overview_url(self):
        return urllib.quote('events/events_officer_overview/' + self.__unicode__().replace("/","|") + "/" + str(self.id))        
    
    def has_student(self, student):
        '''
            Checks if the member/prospective/officer is part of the event by
            checking the room that they're in.
        '''

        if self.which_entries(student):
            return True
        return False

    def which_entries(self, student):
        '''
            Get all the entries that this person (a student object) is a part of.
        '''

        entry_q = self.entry_event_association.filter(student__netid=student.netid)
        guest_q = self.entry_event_association.filter(guest__icontains=student.first_name.lower())\
                                              .filter(guest__icontains=student.last_name.lower())
        return entry_q | guest_q

    def contains_name_in_entry_set(self, fname, lname):
        '''
            Get all the entries that contains this person's name
        '''
        if not fname or not lname:
            return []

        entry_q = self.entry_event_association.filter(student__first_name__icontains=fname.lower())\
                                               .filter(student__last_name__icontains=lname.lower())
        guest_q = self.entry_event_association.filter(guest__icontains=fname.lower())\
                                              .filter(guest__icontains=lname.lower())

        return entry_q | guest_q

    def get_guests(self, student):
        '''
            get the number of guests that a student has
        '''

        return [entry.guest.strip() for entry in self.entry_event_association.filter(student__netid=student.netid) if entry.guest.strip()]

    def __unicode__(self):
        return "%s, %s" % (self.title, self.date.isoformat()[:10])
    
    class Meta:
        ordering = ("title",)




    
    


