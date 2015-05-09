from charterclub.models import *
from django.utils import timezone
from datetime import timedelta

m1 = Member(netid='quanzhou', year=2015, first_name='Quan', last_name='Zhou', house_account=50.0)
m2 = Member(netid='roryf'   , year=2016, first_name='Rory', last_name='Fitzpatrick', house_account=50.0)
m3 = Member(netid='jwhitton', year=2016, first_name='Jeremy', last_name='Whitton', house_account=50.0)
m4 = Member(netid='ajeon', year=2015, first_name='Andrew', last_name='Jeon', house_account=-20.0)

m1.save()
m2.save()
m3.save()
m4.save()
members = [m1, m2, m3]


g1 = Guest(first_name='Julia', last_name='<h1> Who? </h1>', member_association=m1)
g1.save()
guests = [g1]


# ----- spit the data back ------

# First search hit
search = Event.objects.filter(title='Winetasting')[0]

print "Event is:%s" % search.title

for r in search.rooms.all():
    print r.name, ":"
    for m in r.members.all():
        print "  %s %s" % (m.first_name, m.last_name)


# --- Some lookup things---
person = Member.objects.filter(netid='quanzhou')


####################
from charterclub.models import *
from datetime import timedelta

e = Event(title='Formals',
         snippet='yay houseparties!' ,
         date_and_time=timezone.now(),
         end_time=timezone.now() + timedelta(days=1),
         sophomore_signup_start=timezone.now(),
         junior_signup_start   =timezone.now(),
         senior_signup_start   =timezone.now(),
         )
e.save()

room = Room(name='UDR', max_capacity=64)
room.save()
room2 = Room(name='MDR', max_capacity=80)
room2.save()
room3 = Room(name='Great Room', max_capacity=64)
room3.save()

rooms = [room, room2, room3]

e.rooms.add(*rooms)
e.save()



#####
from charterclub.models import *
e = Event.objects.all()[0]
m = Member.objects.all()[0]
m2 = Member.objects.all()[1]
g = Guest.objects.all()[0]
r = Room.objects.all()[0]


e.add_to_event(m,g,r)

