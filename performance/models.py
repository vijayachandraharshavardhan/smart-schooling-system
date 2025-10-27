# performance models placeholder
from django.db import models
from admin_portal.models import Student, Class

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    overall_grade = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.overall_grade}"
