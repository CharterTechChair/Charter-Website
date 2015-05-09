# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cal.models import Entry, EntryAdmin

urlpatterns = patterns('cal.views',
    (r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
    (r"^month/(\d+)/(\d+)/$", "month"),
    (r"^month$", "month"),
    (r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
    (r"^settings/$", "settings"),
    (r"^(\d+)/$", "main"),
    (r"", "main"),
)
