from charterclub.permissions import render
from recruitment.forms import AccountCreationForm


# Flatpages stuff
def recruitment_benefits(request):
    return render(request, "flatpages_default/recruitment_benefits.html")

def recruitment_information(request):
    return render(request, "flatpages_default/recruitment_information.html")    



def create_account(request):
    ''' 
        Create an account using the form
    '''

     # Give them a form to fill out
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            prospective = form.create_account()
            
            return render(request, "recruitment/create_account_success.html", {
                    'prospective' : prospective,
                })
    else:
        form = AccountCreationForm()

        

    return render(request, "recruitment/create_account.html", {
                'form' : form,})