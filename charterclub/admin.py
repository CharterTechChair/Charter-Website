from django.contrib import admin
import forms
from charterclub.models import Person
from charterclub.models import Member
from charterclub.models import Officer
from list_filter import CurrentMembershipListFilter

# Unsure if we should implement this
'''
class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']

admin.site.register(Person, PersonAdmin)
'''



# member editing forms for django-admin. initial entry of a member
# uses netid to fill out other fields automatically
class MemberAdmin(admin.ModelAdmin):
    # What gets shown, and how?
    list_display = ('__unicode__', 'netid', 'year', 'house_account', 'allow_rsvp')
    list_editable = ('house_account', 'allow_rsvp')
    ordering = ['-year', 'last_name', 'first_name']

    # How can we narrow what gets shown?
    search_fields = ['first_name', 'last_name', 'netid', 'year']
    list_filter = (CurrentMembershipListFilter, 'year')
    show_full_result_count = True
    

    

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return forms.NewMemberForm
        else:
            pass
        return super(MemberAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['netid']
        else:
            return []

    # if a new member is created with a netid which already exists in the
    # database, this is effectively blocked from happening.
    def save_model(self, request, obj, form, change):
        if not change:
            existing = Member.objects.filter(netid=obj.netid)
            
            if len(existing) > 0:
                obj = existing[0]
                obj.pk = None
                existing[0].delete()
        obj.save()
    
admin.site.register(Member, MemberAdmin)

# altering officers from with the admin control panel.
# on creating a new officer, you may choose a member and enter their title
class OfficerAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return forms.EditOfficerForm
        else:
            return forms.NewOfficerForm
        return super(OfficerAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['first_name', 'last_name', 'netid']
        else:
            return []

    # if we are creating an officer, we will effectively have to delete
    # and overwrite the member which is becoming an officer
    def save_model(self, request, obj, form, change):
        if not change:
            existing = Member.objects.filter(netid=obj.netid)
            if len(existing) > 0:
                existing[0].delete()
        obj.save()

admin.site.register(Officer, OfficerAdmin)
