from events.models import *
from datetime import timedelta, datetime
from django.core.files import File


monday = (timezone.now() + timedelta(days=-timezone.now().weekday(), weeks=0)).date()

########################################
e1 = Event(title="Pirates of the Caribbean Viewing Party",
     snippet="Yo-ho, Yo-ho, the Pirate's life's for me.", 
     date=timezone.now() + timedelta(days=3))

url = 'media/event_images/pirates.jpg'
image = File(open(url))

e1.image.save(url, image)
r1 = Room(name="TV ROOM", limit=-1, event=e1)



########################################
e2 = Event(title="Christmas Party",
     snippet="For he's a jolly good fellow!", 
     date=timezone.now() + timedelta(days=5),
     is_points_event=True,
     prospective_limit=40)

url = 'media/event_images/christmas.jpg'
image = File(open(url))
e2.image.save(url, image)


r2a = Room(name="Dining room", limit=40, event=e2)
r2b = Room(name="Great Room", limit=40, event=e2)

########################################
e3 = Event(title="Comedian Semiformal",
     snippet="Featuring Andrew Jeon, who is somewhat funny but we all pretend that he's terrible.", 
     date=timezone.now() + timedelta(weeks=3),
     is_points_event=False,
     prospective_limit=40)

r3 = Room(name="Great Room", limit=80, event=e2)

rooms = [r1, r2a, r2b, r3]
events = [e1, e2, e3]



for e in events:
    e.save()

for r in rooms:
    r.save()
