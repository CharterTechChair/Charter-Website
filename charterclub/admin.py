from django.contrib import admin
from django.http import  HttpResponseRedirect
from django.conf.urls import patterns, include, url

import forms

from charterclub.models import Person
from charterclub.models import Member
from charterclub.models import Officer

from charterclub.forms import MemberListForm

from list_filter import CurrentMembershipListFilter

# Form previews
from charterclub.preview import MemberListPreview
from charterclub.forms import MemberListForm, NewMemberForm, EditOfficerForm, NewOfficerForm
from django import forms
# Unsure if we should implement this
'''
class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']

admin.site.register(Person, PersonAdmin)
'''


#################################################################################
# member editing forms for django-admin. initial entry of a member
# uses netid to fill out other fields automatically
#################################################################################
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
            return NewMemberForm
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

    # Adds a list of multiple members
    def add_members(self, request):        
        if request.method == 'POST':

            form = MemberListForm(request.POST)
            if form.is_valid():
                print "yay, form is valid"
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
        else:
            form = MemberListForm()

        # return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return render(request, 'admin/charterclub/member/add_member_list_form.html', {
            'title': 'Add a list of members',
            # 'entry': entry,
            'opts': self.model._meta,
            'form': form,
            # 'root_path': self.admin_site.root_path,
        })

    # Confirms that each member is added or not
    def form_confirmation(self, request):
        labels = {'First Name', 'Last Name', 'NETID', 'House Account Balance', 'Status'}
        table = [['Quan', 'Zhou', 'quanzhou', '$255.00', 'Ready to be Added']]
        # Look at String

        # Look up members in database
        string = request.POST['content']
        # Return results
            # Prospective: old points
            # Added as new student member
            # Member already exists (show data)
        # Note: once prospectives are added to the database, the number of points they had
        #       will be lost
        # Give user to the opportunity to ("update all", "only update new", "cancel")
        return render(request, 'admin/charterclub/member/add_member_list_form_confirmation.html', {
            'title': 'Add a list of members',
            # 'entry': entry,
            'opts': self.model._meta,
            'label' : labels, 
            'table' : table,
            # 'root_path': self.admin_site.root_path,
        })

    

    # Adds the "add_members" to the url
    def get_urls(self):
        urls = super(MemberAdmin, self).get_urls()
        my_urls = patterns("",
            # url(r"add-members/$", self.admin_site.admin_view(self.add_members)),
            # url(r"add-members/confirmation/$", self.admin_site.admin_view(self.form_confirmation)),
            (r'^add-members/$', MemberListPreview(MemberListForm)),
        )

        return my_urls + urls



admin.site.register(Member, MemberAdmin)

#################################################################################
# altering officers from with the admin control panel.
# on creating a new officer, you may choose a member and enter their title
#################################################################################
class OfficerAdmin(admin.ModelAdmin):
    # What gets shown, and how?
    list_display = ('__unicode__',  'position', 'year',)
    list_editable = ('position',)
    ordering = ['position']

    # What gets filtered/searched?
    search_fields = ['first_name', 'last_name', 'netid', 'year', 'position']


    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return EditOfficerForm
        else:
            return NewOfficerForm
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




#################################################################################
# Let's try to do some "fancy" Django Admin here for
# the "add list of members" button
#################################################################################
from django.contrib.admin.views.decorators import staff_member_required
from charterclub.views import render
from charterclub import permissions

# @staff_member_required
# def add_members(request):
#     print "hello world, from add_members in admin.py in the app: charterclub"

#     return render(request, 'admin/charterclub/member/my_own_form.html', {
#      # 'form': form,
#      'error': '',
#      # 'netid':  permissions.get_username(request),
#    })  
#     # return HttpResponseRedirect(request.META["HTTP_REFERER"])



admin.site.register(Officer, OfficerAdmin)
