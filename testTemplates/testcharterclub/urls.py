from django.conf.urls import patterns, include, url
from django.contrib import admin

#Here is a mapping between the pattern in the URL to the function that
#   generates the page.
urlpatterns = patterns('',
    url(
        r'^$',
        'charterclub.views.index',
        name='index'), 

    url(
        r'^index$',
        'charterclub.views.index',
        name='index'),                             
)
