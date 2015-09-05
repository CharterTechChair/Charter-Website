from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class DjangoHTMLCalendar(HTMLCalendar):

    def __init__(self):
        super(DjangoHTMLCalendar, self).__init__()

    # def formatday(self, day, weekday):
    #     if day == 0:
    #         return '<td class="noday">&nbsp;</td>' # day outside month
    #     else:
    #         return '<td class="%s"><a href="%s">%d</a></td>' % (self.cssclasses[weekday], weekday, day)

    # def formatmonth(self, year, month):
    #     self.year, self.month = year, month
    #     return super(DjangoHTMLCalendar, self).formatmonth(year, month)

    # def day_cell(self, cssclass, body):
    #     return '<td class="%s">%s</td>' % (cssclass, body)