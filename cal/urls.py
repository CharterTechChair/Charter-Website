# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cal.models import Entry, EntryAdmin

# urlpatterns = patterns('cal.views',
#     (r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
#     (r"^month/(\d+)/(\d+)/$", "month"),
#     (r"^month$", "month"),
#     (r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
#     (r"^settings/$", "settings"),
#     (r"^(\d+)/$", "main"),
#     (r"", "main"),
# )

urlpatterns = patterns('',
    url(
        r'^/month/(\d+)/(\d+)/(prev|next)/$',
        'cal.views.month',
        name='month'),  
    url(
        r'^/month/(\d+)/(\d+)/$',
        'cal.views.month',
        name='month'),

    # url(
    #     r'^/month$', 
    #     'cal.views.month', 
    #     name='month'),
    url(
        r'^/day/(\d+)/(\d+)/(\d+)/$$', 
        'cal.views.day', 
        name='day'),
    url(
        r'^settings/$', 
        'cal.views.settings', 
        name='settings'),
    url(
        r'^/(\d+)/$$', 
        'cal.views.main', 
        name='cal'),
    url(
        r'',
        'cal.views.main',
        name='cal'),
)