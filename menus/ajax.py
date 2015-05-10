from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def updatemenu(request, date):
    dajax = Dajax()

    dajax.assign("#id_lunch_food", "innerHTML", str(date))

    return dajax.json()
