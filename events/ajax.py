from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
# from events.models import Event
# from crispy_forms.helper import FormHelper
# from events.forms import EventCreateForm
# import datetime
# # uses ajax: whenever the date field in our form is changed, the
# # page loads the event associated with the selection and updates the
# # associated input fields with the current information for that event

# # this encapsulates the server-response part of this process
# @dajaxice_register
# def loadevent(request, event):
#     dajax = Dajax()

#     if event:
#         event = Event.objects.get(pk=event)
#         dajax.assign("[type=checkbox]", "disabled", "disabled")#FormHelper().render_layout(
#     else:       
#         dajax.clear("[type=checkbox]", "disabled")#FormHelper().render_layout(
#         event = Event(title = "", snippet = "")

#     dajax.assign("#id_title", "value", event.title)
#     dajax.assign("#id_snippet", "value", event.snippet)

#     def tstr(date_and_time):
#         if date_and_time:
#             return date_and_time.strftime("%Y-%m-%d %H:%M")
#         else:
#             return ""
        
    
#     dajax.assign("#id_date_and_time", "value", tstr(event.date_and_time))
   
#     dajax.assign("#id_signup_end_time", "value", tstr(event.signup_end_time))
    
#     dajax.assign("#id_sophomore_signup_start", "value", tstr(event.sophomore_signup_start))

    
#     dajax.assign("#id_junior_signup_start", "value", tstr(event.junior_signup_start))
    
#     dajax.assign("#id_senior_signup_start", "value", tstr(event.senior_signup_start))
    
#     #dajax.assign("#div_id_chooserooms", "innerHTML", "")
#     return dajax.json()
