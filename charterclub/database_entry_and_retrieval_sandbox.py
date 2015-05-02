from charterclub.models import *
from django.utils import timezone

m1 = Member(netid='quanzhou', year=2015, first_name='Quan', last_name='Zhou', house_account=0.0)
m2 = Member(netid='roryf'   , year=2016, first_name='Rory', last_name='Fitzpatrick', house_account=0.0)
m3 = Member(netid='jwhitton', year=2016, first_name='Jeremy', last_name='Whitton', house_account=0.0)
m4 = Member(netid='ajeon', year=2015, first_name='Andrew', last_name='Jeon', house_account=-20.0)

m1.save()
m2.save()
m3.save()
m4.save()
members = [m1, m2, m3]

g1 = Guest(first_name='Julia', last_name='<h1> Who? </h1>', member_association=m1)
g1.save()
guests = [g1]


event = Event(title='Winetasting', snippet='Get Ready for Wine-Tazing' , date_and_time=timezone.now())
event.save()

room = Room(name='UDR', max_capacity=15)
room.save()

room.members.add(*members)
room.guests.add(*guests)
room.save()

event.rooms.add(room)
event.save()



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