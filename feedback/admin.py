from django.contrib import admin

# Register your models here.

from feedback.models import FeedbackResponse

class FeedbackResponseAdmin(admin.ModelAdmin):
  readonly_fields = ("responded_by", "response_time")

  def save_model(self, request, obj, form, change):
    obj.responded_by = request.user
    obj.save()

admin.site.register(FeedbackResponse, FeedbackResponseAdmin)
