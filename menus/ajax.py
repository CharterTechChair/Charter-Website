from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from menus.models import MenuItem

@dajaxice_register
def updatemenu(request, date):
    dajax = Dajax()

    menu = MenuItem.objects.filter(date=date)
    if len(menu) > 0:
        menu = menu[0]
    else:
        menu = MenuItem(date = date, lunch_food = "", dinner_food = "")

    dajax.assign("#id_lunch_food", "innerHTML", menu.lunch_food)
    dajax.assign("#id_dinner_food", "innerHTML", menu.dinner_food)

    return dajax.json()
