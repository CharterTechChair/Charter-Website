from django.http import HttpResponse #Allows Django to Respond to Page Requests
from django import template          #Use templates
from django.shortcuts import render  #Quickly render pages from templates
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from object_model import createSophomore, getSophomore
import configuration
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})

