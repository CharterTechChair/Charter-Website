from charterclub.models import Student, Prospective, Member
from events.models import Entry
from django.utils import timezone

class StudentModelViewer(object):
    def __init__(self, student):
        self.student = student

    def get_upcoming_events(self):
        return Entry.get_future_related_entries_for_student(self)

    def get_past_events(self):
        return Entry.get_past_related_entries_for_student(self)


class ProspectiveModelViewer(StudentModelViewer):
    def __init__(self, prospective):
        super(ProspectiveModelViewer, self).__init__(prospective.student)
        self.prospective = prospective

    def get_upcoming_meals(self):
        entries = self.prospective.prospectivemealentry_set.filter(meal__day__gte=timezone.now())
        return [e.meal for e in entries]

    def get_completed_meals(self):
        entries = self.prospective.prospectivemealentry_set.filter(completed=True)  
        return [e.meal for e in entries]