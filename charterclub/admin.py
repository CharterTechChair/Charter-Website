from django.contrib import admin
from charterclub.models import Person, Member

class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']

admin.site.register(Person, PersonAdmin)

# class MemberAdmin(admin.ModelAdmin):
#     fields = ['first_name', 'last_name']

# admin.site.register(Member, MemberAdmin)
