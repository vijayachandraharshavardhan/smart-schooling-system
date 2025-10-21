from django.db import models

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('professional', 'Professional'),
        ('sports', 'Sports'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='achievements/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional: for future features
    highlight = models.BooleanField(default=False)  # if you want to mark some achievements as special
    link = models.URLField(blank=True, null=True)   # optional external link

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
