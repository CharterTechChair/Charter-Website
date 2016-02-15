import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from feedback.forms import FeedbackForm
import charterclub.permissions as permissions
from charterclub.permissions import render
from django.core.mail import send_mail

@permissions.member
def feedback(request):
   now = datetime.datetime.now().date()
   #Generate Feedback Form
   if request.method == 'POST':
     form = FeedbackForm(request.POST)
     if form.is_valid():
        subject = "Anonymous Feedback: " + form.cleaned_data['subject']
        message = form.cleaned_data['anonymous_feedback']
        sender = 'charter.techchair@gmail.com'
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['charter-officers@princeton.edu']
        if cc_myself:
            my_email = permissions.get_username(request) + "@princeton.edu"
            recipients.append(my_email)

        send_mail(subject, message, sender, recipients, fail_silently=False)
        return redirect('/feedback/feedback_thanks/')
   else:
      form = FeedbackForm()

   return render(request, 'feedback/feedback.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': permissions.get_username(request),
   })  

@permissions.member
def thanks(request):
    now = datetime.datetime.now().date()

    return render(request, "feedback/thanks.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
    })

3783-4853-58661006

October 2020
452