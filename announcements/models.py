from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    attachment = models.FileField(upload_to="announcements/", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
