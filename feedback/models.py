from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class FeedbackResponse(models.Model):
  feedback_description = models.TextField()
  response = models.TextField()
  display_user = models.BooleanField(default=True)

  responded_by = models.ForeignKey(User)
  response_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{desc} (by {poster} at {t})'.format(
      desc=self.feedback_description,
      poster=self.responded_by.username,
      t=self.response_time.isoformat())
