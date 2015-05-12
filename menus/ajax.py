from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from menus.models import MenuItem

# uses ajax: whenever the date field in our form is changed, the
# page loads the menu associated with that date and updates the
# associated text_area with the current information for that menu

# this encapsulates the server-response part of this process
@dajaxice_register
def updatemenu(request, date):
    dajax = Dajax()

    if date:
        menu = MenuItem.objects.filter(date=date)
    else:
        menu = []
    
    if len(menu) > 0:
        menu = menu[0]
    else:
        menu = MenuItem(date = date, lunch_food = "", dinner_food = "")

    dajax.assign("#id_lunch_food", "value", menu.lunch_food)
    dajax.assign("#id_dinner_food", "value", menu.dinner_food)

    return dajax.json()
