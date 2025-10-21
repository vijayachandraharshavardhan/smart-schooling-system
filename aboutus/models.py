from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    document = models.FileField(upload_to='about_docs/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title or f"AboutUs Document ({self.id})"
