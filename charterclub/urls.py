from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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
    url(
        r'^calendar$',
        'charterclub.views.calendar',
        name='calendar'),
    url(
        r'^calendar2$',
        'charterclub.views.calendar2',
        name='calendar2'),
    url(
        r'^faceboard$',
        'charterclub.views.faceboard',
        name='faceboard'),
    url(
        r'^menu$',
        'charterclub.views.menu',
        name='menu'),
    url(
        r'^profile$',
        'charterclub.views.profile',
        name='profile'),
    url(
        r'^login$',
        'charterclub.views.login',
        name='login'),
    url(
        r'^history$',
        'charterclub.views.history',
        name='history'),
    url(
        r'^song$',
        'charterclub.views.song',
        name='song'),
    url(
        r'^constitution$',
        'charterclub.views.constitution',
        name='constitution'),
    url(
        r'^help$',
        'charterclub.views.help',
        name='help'),
    url(
        r'^#$',
        'charterclub.views.underconstruction',
        name='#'),
    # for CAS
    url(
        r'^accounts/login/$',
        'django_cas.views.login'),
    url(
        r'^accounts/logout/$',
        'django_cas.views.logout'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)