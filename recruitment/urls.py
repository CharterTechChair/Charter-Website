from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # url(
    #     r'^benefits$',
    #     'recruitment.views.recruitment_benefits',
    #     name='recruitment_benefits'),
    # url(
    #     r'^information$',
    #     'recruitment.views.recruitment_information',
    #     name='recruitment_information'),
    # url(
    #     r'^recruitment/create_account$',
    #     'recruitment.views.create_account',
    #     name='create_account'),
    # url(
    #     r'^mailing_list$',
    #     'recruitment.views.mailing_list',
    #     name='mailing_list'),
    url(
        r'^mailing_list_view$',
        'recruitment.views.mailing_list_view',
        name='mailing_list_view'),
    url(
        r'^prospective_meal_list/([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/$',
        'recruitment.views.prospective_meal_list',
        name='prospective_meal_list_day'),
    url(
        r'^prospective_meal_list$',
        'recruitment.views.prospective_meal_list',
        name='prospective_meal_list'),
    url(
        r'^meal_mailing_list/([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/$',
        'recruitment.views.meal_mailing_list',
        name='meal_mailing_list_day'),
    url(
        r'^meal_mailing_list$',
        'recruitment.views.meal_mailing_list',
        name='meal_mailing_list'),
)
