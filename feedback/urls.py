from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(
        r'^/form$',
        'feedback.views.feedback',
        name='feedback'), 
    url(
        r'^/thanks$',
        'feedback.views.thanks',
        name='thanks'),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)