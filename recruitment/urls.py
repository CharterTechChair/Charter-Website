from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^benefits$', 
        'recruitment.views.recruitment_benefits', 
        name='recruitment_benefits'),
    url(
        r'^information$', 
        'recruitment.views.recruitment_information', 
        name='recruitment_information'),
    url(
        r'^create_account$', 
        'recruitment.views.create_account', 
        name='create_account'),
)