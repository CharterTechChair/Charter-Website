# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from views import CalendarJsonListView

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('django_bootstrap_calendar.views',
       url(
          r'^json/$',
          CalendarJsonListView.as_view(),
          name='calendar_json'
       ),
       url(
          r'^$',
          'calendar',
          name='calendar'
       ),
       url(
          r'^add$',
          'add',
          name='add'),
                       )
