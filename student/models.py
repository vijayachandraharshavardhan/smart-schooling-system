from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    student_class = models.ForeignKey(
        'teacher.ClassSection',  # Reference to teacher app
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

    class Meta:
        ordering = ['roll_number']  # Optional: for cleaner student lists
