from django.utils import timezone

from events.models import Entry
from charterclub.models import Prospective
from recruitment.models import ProspectiveMealEntry


class StudentViewer:
    def __init__(self, student):
        self.student = student

    def get_future_event_entries(self):
        return Entry.get_future_event_entries_for_student(self)

    def get_past_event_entries(self):
        return Entry.get_past_event_entries_for_student(self)

class ProspectiveViewer:
    def __init__(self, prospective):
        super(ProspectiveViewer, self).__init__(prospective.student)
        self.prospective=prospective

    def get_upcoming_meals(self):
        '''
            Gets the future meals for this prospective
        '''
        entries = self.prospective.prospectivemealentry_set.filter(meal__day__gte=timezone.now(), completed=False)
        return [e.meal for e in entries]

    def get_completed_meals(self):
        '''
            Gets the completed meals. 
        '''
        entries = self.prospective.prospectivemealentry_set.filter(completed=True)
        return [e.meal for e in entries]

    def get_future_event_entries(self):
        ProspectiveMealEntry.get_future_related_entries_for_student()
