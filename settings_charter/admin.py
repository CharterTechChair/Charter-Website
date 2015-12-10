from django.contrib import admin
from settings_charter.models import CharterClubSettings
# Register your models here.


class CharterClubSettingsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'Explanation', 'Special_Note')

    def Special_Note(self, obj):
        return "To edit this object (which controls the defaults), click on it."
    def Explanation(self, obj):
        return "These settings control some of the default number of stuff that a new member, prospective, officer, etc has when it is created."

admin.site.register(CharterClubSettings, CharterClubSettingsAdmin)