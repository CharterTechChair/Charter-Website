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
        form = EventEntryForm(event=event)
    # If the form is filled out, check it
    else:
        form = EventEntryForm(request.POST, event=event)

        if form.is_valid():
            data =  form.cleaned_data
            # Lookup the Member   
            lookup_m =  Member.objects.filter(first_name=data['first_name'],
                                             last_name =data['last_name'])
            if not lookup_m:
                raise Exception('Error: Member with netid "%s" not found in member database' % request['netid']) 
            member = lookup_m[0]


            # If there's a guest, either find the guest or make one
            if data['guest_first_name'] or data['guest_last_name']:
                lookup_g =  Guest.objects.filter(first_name=data['guest_first_name'],
                                                last_name =data['guest_last_name'])
                # Try to find the guest - else, look them up
                if lookup_g:
                   guest = lookup_g[0]
                else:
                    guest = Guest(first_name=data['guest_first_name'], 
                              last_name =data['guest_last_name'],
                              member_association=member)
                    guest.save()
            else:
                guest = None

            # Now try to add a person 
            event.add_to_event(member, guest, form.cleaned_data['room_choice'])

            # subject = 'Congraduations!'
            # body = 'You just signed up for "%s" on %s' % (event.title, 
            #                                                 event.date_and_time.isoformat()[:10])
            # return render(request, 'standard_message.html', {
            #       'subject' : 'Congrats',
            #       'body'    : body
            # })
            return redirect('events')
    return render(request, 'events_form.html', {
        'form': form,
        'event': event,
        'error': '',
        'netid': permissions.get_username(request),
    })



# def events_signup_choose(request):
#     if request.method == 'POST':
#         form = EventChoiceForm(request.POST)

#         if form.is_valid():
#           data = form.cleaned_data
#           event = data['event_choice']
#           return HttpResponseRedirect(event.get_signup_url())
#     else:
#         form = EventChoiceForm()

#     return render(request, 'form.html', {
#           'form' : form,
#     })

#     return render(request, 'events_signup_choose.html',{})

# def events_view_choose(request):
#   if request.method == 'POST':
#       form = EventChoiceForm(request.POST)

#       if form.is_valid():
#         data = form.cleaned_data
#         event = data['event_choice']
#         return HttpResponseRedirect(event.get_view_url())
#   else:
#     form = EventChoiceForm()

#   return render(request, 'form.html', {
#         'form' : form,
#     })

#   return render(request, 'events_signup_choose.html',{})

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
        wt_obj = event_search[0]
        return render(request, 'events_view.html', {
                     'error': '',
                     'netid': permissions.get_username(request),
                     'room_list' : wt_obj.to_JSON()['rooms'],
        })  
    # return HttpResponse("Hello, world. You're at a events view")

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
        if event.has_person(member):
            event.remove_from_event(member)
            return redirect('events')
        else:
            return render(request, 'standard_message.html', {
                'subject' : 'No RSVP found',
                'message' : "are you sure you had RSVP'd to this event?",
        })




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

    has_rsvp = [e.has_person(member) for  e in events]
    event_msg = []
    for event, rsvp in zip(events, has_rsvp):
        if rsvp:
            room  =  event.get_room_of_person(member)
            guest =  room.get_guest_of_member(member)

            msg = "You" 
            if guest:
                msg += ' and your guest "%s %s"' % (guest.first_name, guest.last_name)
            msg +=  " are in the %s." % room
        else:
            msg = "You have not RSVP'd for this event."

        event_msg.append(msg)
     

    return render(request, 'events_list.html', {
      'error': '',
      'netid': permissions.get_username(request),
      'events_info': zip(events, has_rsvp, event_msg) ,
    })  
 
def thanks_create(request):
  now = datetime.datetime.now().date()
  return render(request, "thanks_create.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
  })

def thanks_signup(request):
  now = datetime.datetime.now().date()
  return render(request, "thanks_signup.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
  })
