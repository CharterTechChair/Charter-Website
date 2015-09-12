from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^information$', 
        'recruitment.views.information', 
        name='recruitment_information'),

)