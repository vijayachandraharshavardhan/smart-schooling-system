from django.db import models

class ContactInfo(models.Model):
    principal_name = models.CharField(max_length=255)
    principal_email = models.EmailField(blank=True, null=True)
    principal_mobile = models.CharField(max_length=15, blank=True, null=True)
    correspondent_name = models.CharField(max_length=255)
    correspondent_email = models.EmailField(blank=True, null=True)
    correspondent_mobile = models.CharField(max_length=15, blank=True, null=True)
    management_email = models.EmailField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)  # ✅ this line fixes your error

    def __str__(self):
        return self.principal_name
