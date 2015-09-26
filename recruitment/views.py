from charterclub.permissions import render
import charterclub.permissions as permissions
from recruitment.forms import AccountCreationForm #, MailingListForm


# # Flatpages stuff
# def recruitment_benefits(request):
#     return render(request, "flatpages_default/recruitment_benefits.html")

# def recruitment_information(request):
#     return render(request, "flatpages_default/recruitment_information.html")    



def create_account(request):
    ''' 
        Display Recruitment information
    '''

    return render(request, "recruitment/create_account.html")

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

    return render(request, "mailinglist_view.html", {
       'plist': plist,
       'netid': permissions.get_username(request)
    })