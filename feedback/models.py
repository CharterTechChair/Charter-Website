from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class FeedbackResponse(models.Model):
  feedback_description = models.TextField()
  response = models.TextField()

  responded_by = models.ForeignKey(User)
  response_time = models.DateTimeField(auto_now_add=True)
