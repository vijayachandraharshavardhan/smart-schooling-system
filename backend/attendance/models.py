from django.db import models
from django.utils import timezone
from admin_portal.models import Teacher

# -----------------------------
# Class & Section
# -----------------------------
class ClassSection(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    class Meta:
        unique_together = ('class_name', 'section')
        ordering = ['class_name', 'section']
        verbose_name = "Class Section"
        verbose_name_plural = "Class Sections"

    def __str__(self):
        return f"{self.class_name} - {self.section}"


# -----------------------------
# Subject
# -----------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_section = models.ForeignKey(
        ClassSection, on_delete=models.CASCADE, related_name="subjects"
    )

    class Meta:
        unique_together = ('name', 'class_section')
        ordering = ['class_section', 'name']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return f"{self.name} ({self.class_section})"


# -----------------------------
# Attendance
# -----------------------------
class Attendance(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(
        'student.Student',
        on_delete=models.CASCADE,
        related_name='daily_attendance'
    )
    date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default="Present"
    )

    class Meta:
        unique_together = ('class_section', 'subject', 'student', 'date')
        ordering = ['-date']
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date} ({self.status})"
