# Some standard imports here
import datetime, urllib, pdb

from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.dateparse import parse_date

from charterclub.models import *
from charterclub.forms import *
from charterclub.views import render
import charterclub
import charterclub.permissions as permissions

from events.models import Event, Room
from events.forms import EventEntryForm, EventCreateForm, EventChoiceForm

# ------------------------------------------------------------
# Responsible for creating entries to events. 
# 
# Chooses the event from the title and date parsed from the url. 
# ------------------------------------------------------------
@permissions.member
def events_entry(request, title, date):
  # Look for the event
    start = parse_date(date)
    end = start + datetime.timedelta(days=1)
    event_search = Event.objects.filter(title=urllib.unquote(title), date_and_time__range = [start, end])


    # If we don't find the event then send them the error message
    if not event_search:  
        subject = 'No Signups Available'
        body = "Looks like there are no upcoming events with signups at the moment."
        return render(request, 'standard_message.html', {
                'subject' : subject,
                'body'    : body,
        })
    event = event_search[0]
    # If we do find it, give them the form
    if request.method != 'POST':
        form = EventEntryForm(event=event, netid=permissions.get_username(request))
    # If the form is filled out, check it
    else:
        form = EventEntryForm(request.POST, event=event, netid=permissions.get_username(request))
        if form.is_valid():
            data =  form.cleaned_data
            # Lookup the Member   
            member = Member.objects.filter(netid=permissions.get_username(request))[0]
            guest_s = "%s %s" % (form.cleaned_data['guest_first_name'], form.cleaned_data['guest_last_name'])
            guest_s = guest_s.strip()

            # Now try to add a person 
            event.add_to_event(member, guest_s, form.cleaned_data['room_choice'])

            return redirect('events')
    return render(request, 'events_form.html', {
        'form': form,
        'event': event,
        'error': '',
        'netid': permissions.get_username(request),
    })

@permissions.member
def events_view(request, title, date):
    start = parse_date(date)
    end = start + datetime.timedelta(days=1)
    event_search = Event.objects.filter(title=urllib.unquote(title), date_and_time__range = [start, end])
    
    # If we don't find the event then send them the error message
    if not event_search:  
        subject = "Doesn't look like this event exists"
        body = "Checkout "
        return render(request, 'standard_message.html', {
                'subject' : subject,
                'message' : body,
        })

    # If we find the event, show it to them
    else:
        event = event_search[0]

        return render(request, 'events_view.html', {
                     'error': '',
                     'netid': permissions.get_username(request),
                     'room_list' : event.to_JSON()['rooms'],
        })  

    # return HttpResponse("Hello, world. You're at a events view")
@permissions.member
def events_unrsvp(request, title, date):
    start = parse_date(date)
    end = start + datetime.timedelta(days=1)
    event_search = Event.objects.filter(title=urllib.unquote(title), date_and_time__range = [start, end])
    
    # If we don't find the event then send them the error message
    if not event_search:  
        subject = "Doesn't look like this event exists"
        body = "Checkout "
        return render(request, 'standard_message.html', {
                'subject' : subject,
                'message' : body,
        })
    else:
        # Lookup the Member   
        lookup_m =  Member.objects.filter(netid=permissions.get_username(request))
        event = event_search[0]

        if not lookup_m:
            raise Exception('Error: Member with netid "%s" not found in member database' % request['netid']) 
        member = lookup_m[0]

        # If the member is in the room, take the person out. 
        if event.has_member(member):
            event.remove_from_event(member)
            return redirect('events')
        else:
            return render(request, 'standard_message.html', {
                'subject' : 'No RSVP found',
                'message' : "are you sure you had RSVP'd to this event?",
        })



@permissions.officer
def events_create(request):
   #Generate Event Form
   if request.method == 'POST':
     form = EventCreateForm(request.POST)
     if form.is_valid():
        form.make_event()
        return HttpResponseRedirect('thanks_create') # Redirect after POST
   else:
      form = EventCreateForm()

   return render(request, 'events_create.html', {
     'form': form,
     'error': '',
     'netid': permissions.get_username(request),
     # 'netid': permissions.get_username(request),
   })  

@permissions.member
def events_list(request):
    events = Event.objects.order_by('date_and_time')
    member = Member.objects.filter(netid=permissions.get_username(request))[0]

    has_rsvp = [e.has_member(member) for  e in events]
    event_msg = []
    for event, rsvp in zip(events, has_rsvp):
        if rsvp:
            room    =  event.get_room_of_member(member)
            listing =  room.get_seating(member)

            msg = "You" 
            if listing.guest:
                msg += ' and your guest "%s"' % (listing.guest)
            msg +=  " are in the %s." % room
        else:
            msg = "You have not RSVP'd for this event."

        event_msg.append(msg)
     

    return render(request, 'events_list.html', {
      'error': '',
      'netid': permissions.get_username(request),
      'events_info': zip(events, has_rsvp, event_msg) ,
    })  
 
@permissions.officer
def thanks_create(request):
  now = datetime.datetime.now().date()
  return render(request, "thanks_create.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
  })

@permissions.member
def thanks_signup(request):
  now = datetime.datetime.now().date()
  return render(request, "thanks_signup.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
  })
