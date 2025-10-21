from django.db import models

class Rank(models.Model):
    student_name = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='rank_photos/', blank=True, null=True)
    position = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position}. {self.student_name}"
