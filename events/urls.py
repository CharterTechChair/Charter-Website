from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^/signup$',
        'events.views.events_choose',
        name='events'),  
    url(
        r'^/signup/(.+)/([0-9]{4}-[0-9]{2}-[0-9]{2})',
        'events.views.events_entry',
        name='event_entry'),

    url(
        r'^/view$', 
        'events.views.events_view', 
        name='events_view'),
    url(
        r'^/create$', 
        'events.views.events_create', 
        name='events_create'),
    url(
        r'^/list$', 
        'events.views.events_list', 
        name='events_list'),
    url(
        r'^/create_social$', 
        'events.views.socialevent_create', 
        name='socialevent_create'),
    url(
        r'^/thanks_create$',
        'events.views.thanks_create',
        name='thanks_create'),
    url(
        r'^/thanks_signup$',
        'events.views.thanks_signup',
        name='thanks_signup'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
