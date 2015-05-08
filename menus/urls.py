from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(
        r'^/view$',
        'menus.views.menu',
        name='menu'),
    url(
        r'^/input$',
        'menus.views.menu_input',
        name='menu_input'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)