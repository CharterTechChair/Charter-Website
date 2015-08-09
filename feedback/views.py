import datetime
from charterclub.views import render
from django.http import HttpResponse, HttpResponseRedirect

from feedback.forms import FeedbackForm
import charterclub.permissions as permissions

def feedback(request):
   now = datetime.datetime.now().date()
   #Generate Feedback Form
   if request.method == 'POST':
     form = FeedbackForm(request.POST)
     if form.is_valid():
        subject = 'Anonymous Feedback'
        message = form.cleaned_data['anonymous_feedback']
        sender = 'charter.techchair@gmail.com'
        # cc_myself = form.cleaned_data['cc_myself']

        recipients = ['charter-officers@princeton.edu']
        # if cc_myself:
        #     recipients.append(sender)

        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients, fail_silently=False)
        return HttpResponseRedirect('thanks') # Redirect after POST
   else:
      form = FeedbackForm()

   return render(request, 'feedback/feedback.html', {
     'current_date': now,
     'form': form,
     'error': '',
     'netid': permissions.get_username(request),
   })  

def thanks(request):
    now = datetime.datetime.now().date()
    return render(request, "feedback/thanks.html", {
     'current_date': now,
     'error': '',
     'netid': permissions.get_username(request),
    })