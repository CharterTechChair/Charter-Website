from charterclub.models import *
from events.models import *

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

e = Event(title='Formals',
         snippet='yay houseparties!' ,
         date_and_time=timezone.now(),
         end_time=timezone.now() + timedelta(days=1),
         sophomore_signup_start=timezone.now(),
         junior_signup_start   =timezone.now(),
         senior_signup_start   =timezone.now(),
         )
e.save()

room = Room(name='UDR', max_capacity=15)
room.save()
room2 = Room(name='MDR', max_capacity=3)
room2.save()
room3 = Room(name='Great Room', max_capacity=15)
room3.save()

rooms = [room, room2, room3]

e.rooms.add(*rooms)
e.save()