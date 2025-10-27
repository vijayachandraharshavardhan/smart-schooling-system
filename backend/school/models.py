from django.db import models

class SchoolProfile(models.Model):
    school_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    principal_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    correspondent_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)  # ✅ add this

    def __str__(self):
        return self.school_name
