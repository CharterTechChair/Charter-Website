from django.shortcuts import render
import models
from models import Officer
from models import Member
from models import Student

def officer(func):
    def check_o(request, *args, **kwargs):
        if not check_officer(request):
            return render(request, "permission_denied.html",
                          {"required_permission": "officer"})
        return func(request, *args, **kwargs)
    return check_o

def member(func):
    def check_m(request, *args, **kwargs):
        if not check_member(request):
            return render(request, "permission_denied.html",
                          {"required_permission": "member"})
        return func(request, *args, **kwargs)
    return check_m

def sophomore(func):
    def check_s(request, *args, **kwargs):
        if not check_sophomore(request):
            return render(request, "permission_denied.html",
                          {"required_permission": "sophomore"})
        return func(request, *args, **kwargs)
    return check_s

from django.conf import settings
# get the username of the currently CAS logged-in user.
# if there is no currently logged-in user, return an empty string
# if the application is in debug mode, assume that CAS is non-functional,
# and return a test value (in this case jwhitton)
def get_username(request):
    if settings.CAS_DISABLED:
        return "testuser"
    else:
        if not request.user.username:
            return ""
        else:
            return request.user.username

# check if the currently CAS logged-in user is an officer, returning
# true if so and false otherwise.
def check_officer(request):
    netid = get_username(request)
    if netid == "":
        return False

    user = Officer.objects.filter(netid=netid)

    if len(user) == 0:
        return False
    else:
        return True
    
# check if the currently CAS logged-in user is a member, returning
# true if so and false otherwise.
def check_member(request):
    netid = get_username(request)
    if netid == "":
        return False

    user = Member.objects.filter(netid=netid)

    if len(user) == 0:
        return False
    else:
        return True

import datetime
import ldap_student_lookup
# check if the currently CAS logged-in user is a sophomore, returning
# true if so and false otherwise.
def check_sophomore(request):
    netid = get_username(request)
    if netid == "":
        return False

    if len(ldap_student_lookup.ldap_lookup("netid=" + netid)) == 0:
        return False
    
    student = ldap_student_lookup.get_student_info(netid)

    # check that the student's graduation year indicates they are currently
    # a sophomore. e.g. a student graduating in 2017 is a sophomore if we are
    # currently in the latter half of 2014 or the beginning half of 2015.
    today = datetime.date.today()
    year = (today + datetime.timedelta(days = 6*30))
    if student.year == (year + 2):
        return True
    return False


