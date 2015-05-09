from django.contrib import admin
import forms
from charterclub.models import Person
from charterclub.models import Member
from charterclub.models import Officer

# class PersonAdmin(admin.ModelAdmin):
#     fields = ['first_name', 'last_name']

# admin.site.register(Person, PersonAdmin)

class MemberAdmin(admin.ModelAdmin):    
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

    def save_model(self, request, obj, form, change):
        if not change:
            existing = Member.objects.filter(netid=obj.netid)
            
            if len(existing) > 0:
                obj = existing[0]
                obj.pk = None
                existing[0].delete()
        obj.save()
    
admin.site.register(Member, MemberAdmin)

class OfficerAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return forms.EditOfficerForm
        else:
            return forms.NewOfficerForm
        return super(OfficerAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['first_name', 'last_name']
        else:
            return []
    
    def save_model(self, request, obj, form, change):
        if not change:
            existing = Member.objects.filter(netid=obj.netid)
            if len(existing) > 0:
                existing[0].delete()
        obj.save()

admin.site.register(Officer, OfficerAdmin)
