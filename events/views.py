# Some standard imports here
import datetime, urllib

from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

from charterclub.models import *
from charterclub.forms import *
from charterclub.views import render
import charterclub
import charterclub.permissions as permissions

from events.models import Event
from events.forms import EventEntryForm, EventCreateForm, AddSocialEventForm, EventChoiceForm

def events_entry(request, title, date):
    start = datetime.datetime.strptime(date, "%Y-%m-%d")
    end = start + datetime.timedelta(days=1)

    # Look for the event
    event_search = Event.objects.filter(title=title, date_and_time__range = [start, end])

    if not event_search:
        subject = 'No Signups Available'
        body = "Looks like there are no upcoming events with signups at the moment."
        return render(request, 'standard_message.html', {
                'subject' : subject,
                'body'    : body,
          })
    else:
        # Give them the form
        if request.method != 'POST':
            form = EventEntryForm(event=event_search[0])
            return render(request, 'events.html', {
                'form': form,
                'error': '',
                'netid': permissions.get_username(request),
            })
        # If the form is filled out, check it
        else:
            form = EventEntryForm(request.POST, event=event_search[0])

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
            event_search[0].add_to_event(member, guest, form.cleaned_data['room_choice'])

        return redirect('thanks_signup')


def events_choose(request):
  if request.method == 'POST':
      form = EventChoiceForm(request.POST)

      if form.is_valid():
        data = form.cleaned_data
        event = data['event_choice']
        event_s = "%s/%s" % (event.title, event.date_and_time.isoformat()[:10])
        return HttpResponseRedirect('/events/signup/' + urllib.quote(event_s))
  else:
    form = EventChoiceForm()

  return render(request, 'form.html', {
        'form' : form,
    })

  return render(request, 'events_choose.html',{})

def events_view(request):
    now = datetime.datetime.now().date()

    wt_obj = Event.objects.filter(title='Formals')[0]
    return render(request, 'events_view.html', {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
     'room_list' : wt_obj.to_JSON()['rooms'],
    })  
    # return HttpResponse("Hello, world. You're at a events view")


def events_create(request):
   now = datetime.datetime.now().date()
   #Generate Event Form
   if request.method == 'POST':
     form = EventCreateForm(request.POST)
     if form.is_valid():
        data = form.cleaned_data
        title = data['title']
        snippet = data['description']
        date_and_time = data['date_and_time']
        soph = data['sophomore_signup_start']
        jr = data['junior_signup_start']
        sr = data['senior_signup_start']
        rooms = data['rooms']

        event = Event(title=title, snippet=snippet , date_and_time=date_and_time,
          sophomore_signup_start=soph, junior_signup_start=jr, senior_signup_start=sr,
          end_time=now)
        event.save()

        for r in rooms:
          room = Room(name=r, max_capacity=15)
          room.save()
          event.rooms.add(room)
          event.save()


        return HttpResponseRedirect('thanks_create') # Redirect after POST
   else:
      form = EventCreateForm()

   return render(request, 'events_create.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': 'roryf',
     # 'netid': permissions.get_username(request),
   })  

def events_list(request):
   now = datetime.datetime.now().date()

   ev = Event.objects.all()

   return render(request, 'events_list.html', {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
     'events_list': ev ,
   })  

def socialevent_create(request):
    now = datetime.datetime.now().date()
    #Generate Event Form
    if request.method == 'POST':
        form = AddSocialEventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            socialevent = SocialEvent(title=data['title'], snippet=data['snippet'], 
              date_and_time=data['date_and_time'], end_time=data['end_time'])
            socialevent.save()
            print socialevent

            return HttpResponseRedirect('calendar') # Redirect after POST
    else:
        form = AddSocialEventForm()

    return render(request, 'events_create.html', {
                 'current_date': now,
                 'form': form,
                 'error': '',
                 'netid': permissions.get_username(request),
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
