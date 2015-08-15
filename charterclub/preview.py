from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from charterclub.models import Member, Prospective

# from myapp.models import SomeModel

########################################################################
# A form Preview, taken from 
# https://docs.djangoproject.com/en/1.7/ref/contrib/formtools/form-preview/
########################################################################
class MemberListPreview(FormPreview):
    form_template = 'admin/charterclub/member/add_member_list_form.html'
    preview_template = 'admin/charterclub/member/form_preview.html'

    # Renders the preview section of the form
    def preview_post(self, request):
        "Validates the POST data. If valid, displays the preview page. Else, redisplays form."
        f = self.form(request.POST, auto_id=self.get_auto_id())
        context = self.get_context(request, f)
        if f.is_valid():
            self.process_preview(request, f, context)
            context['hash_field'] = self.unused_name('hash')
            context['hash_value'] = self.security_hash(request, f)
            context['quanbar'] = 'hello, Quan!'
            context['results'] = f.parse_content()
            # context['opts'] = self.model._meta,

            return render_to_response(self.preview_template, context, context_instance=RequestContext(request))
        else:
            return render_to_response(self.form_template, context, context_instance=RequestContext(request))

    # Execute this when the submit button is pressed
    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        f = self.form(request.POST, auto_id=self.get_auto_id())
        if f.is_valid():
            f.submit_content()

        return HttpResponseRedirect('/admin/charterclub/member/')
