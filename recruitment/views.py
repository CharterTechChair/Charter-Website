from charterclub.permissions import render
import charterclub.permissions as permissions
from recruitment.forms import AccountCreationForm #, MailingListForm
from charterclub.models import Prospective
from kitchen.models import Brunch, Lunch, Dinner

from django.utils import timezone
from django.utils.dateparse import parse_date

import datetime

# # Flatpages stuff
# def recruitment_benefits(request):
#     return render(request, "flatpages_default/recruitment_benefits.html")

# def recruitment_information(request):
#     return render(request, "flatpages_default/recruitment_information.html")



# def create_account(request):
#     '''
#         Display Recruitment information
#     '''

#     return render(request, "recruitment/create_account.html")

# def mailing_list(request):
#     if request.method == 'POST':
#       form = MailingListForm(request.POST)
#       if form.is_valid():
#         form.add_soph()

#         return HttpResponseRedirect('contactus')

#     else:
#       form = MailingListForm()


#     return render(request, 'recruitment/mailinglist.html', {
#        'form': form,
#        'netid': permissions.get_username(request),
#      })

# view the list of people who have signed up for our mailing list.
# should probably implement an actual listserv of some description

# at some point
@permissions.officer
def mailing_list_view(request):
    plist = Prospective.objects.filter(mailing_list=True)

    return render(request, "recruitment/mailinglist_view.html", {
       'plist': plist,
       'netid': permissions.get_username(request)
    })

@permissions.officer
def prospective_meal_list_day(request, is_mailing_list, date):
    officer = permissions.get_student(request).cast()
    target = parse_date(date)

    if not target:
        return render(request, 'standard_message.html', {
            'subject': 'Oops, looks like something went wonky.',
            'body' : 'Could note parse_date from "%s"' % (date)

    })

    prev_day = target + datetime.timedelta(days=-1)
    next_day = target + datetime.timedelta(days=1)

    if target.weekday () in range(0,5):
        meal_classes = [Lunch, Dinner]
    else:
        meal_classes = [Brunch, Dinner]

    meal_entries = [lookup_meal_entries(m, target) for m in meal_classes]

    entries = {c.__name__:m for c,m in zip(meal_classes, meal_entries)}

    if is_mailing_list:
        html_string = 'recruitment/meal_mailing_list.html'
    else:
        html_string = 'recruitment/prospective_meal_list.html'
    return render(request, 'recruitment/prospective_meal_list.html', {
        'entries' : entries,
        'officer' : officer,
        'next_day' : next_day,
        'prev_day' : prev_day,
        'time' : timezone.now(),
    })

def prospective_meal_list(request):
    return prospective_meal_list_day(request, False, timezone.now().date().isoformat())

def meal_mailing_list(request):
    return prospective_meal_list_day(request, True, timezone.now().date().isoformat())

def lookup_meal_entries(meal_class, target):
    meal = meal_class.objects.filter(day=target)

    if meal:
        ans = []
        for m in meal:
            ans.extend([e for e in m.prospectivemealentry_set.all()])
        return ans
    else:
        return []










# @permissions.officer
# def print_meals(request):

#     return render(request, "prospective_meal_view.html", {

#         })
