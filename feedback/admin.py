from django.contrib import admin

# Register your models here.

from feedback.models import FeedbackResponse

class FeedbackResponseAdmin(admin.ModelAdmin):
  exclude = ("responded_by",)

  def save_model(self, request, obj, form, change):
    obj.responded_by = request.user
    obj.save()

admin.site.register(FeedbackResponse, FeedbackResponseAdmin)
