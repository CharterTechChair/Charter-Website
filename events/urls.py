from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^$', 
        'events.views.events_list', 
        name='events_list'),

    url(
        r'^signup/(.+)/([0-9]+)',
        'events.views.events_signup', 
        name='events_signup'),
    url(
        r'^delete/(.+)/([0-9]+)',
        'events.views.entry_delete', 
        name='entry_delete'),
    url(
        r'^change/(.+)/([0-9]+)',
        'events.views.entry_change_answers', 
        name='entry_change_answers'),
    url(
        r'^guest_change/(.+)/([0-9]+)',
        'events.views.entry_guest_change', 
        name='entry_guest_change'),
    url(
        r'^room_change/(.+)/([0-9]+)',
        'events.views.entry_room_change', 
        name='entry_room_change'),
    url(
        r'^events_officer_overview/(.+)/([0-9]+)',
        'events.views.events_officer_overview', 
        name='events_officer_overview'),

#     url(
#         
#         'events.views.events_entry',
#         name='event_entry'),

#     url(
#         r'^view/(.+)/([0-9]{4}-[0-9]{2}-[0-9]{2})',
#         'events.views.events_view', 
#         name='events_view'),
#     url(
#         r'^unrsvp/(.+)/([0-9]{4}-[0-9]{2}-[0-9]{2})',
#         'events.views.events_unrsvp', 
#         name='events_unrsvp'),
#     url(
#         r'^create$', 
#         'events.views.events_create', 
#         name='events_create'),
#     url(
#         r'^thanks_create$',
#         'events.views.thanks_create',
#         name='thanks_create'),
)

# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
