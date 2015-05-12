'''
    random_populate_events.py

    written by Quan zhou on May 12, 2015

    Randomly populates events with members. They should be pasted into 
    `python manage.py shell`

    Use this judiciously. 
'''
for event in Event.objects.all():
    max_people = sum([r.max_capacity for r in event.rooms.all()]) 
    max_people = min(max_people, 91)
    people_r = random.sample(Member.objects.all(), max_people*4/5)

    while people_r:
        random_room = random.sample(event.rooms.all(), 1)[0]
        p_guest = 0.8

        member = people_r.pop()
        guest_s = ""

        if (random.random() < p_guest) and people_r:
            guest = people_r.pop()
            guest_s = "%s %s" % (guest.first_name, guest.last_name)

        e.add_to_event(member, guest_s, random_room)
        print "%s with guest %s was added to %s" % (member, guest_s, random_room)


