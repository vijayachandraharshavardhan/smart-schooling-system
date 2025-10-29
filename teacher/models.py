from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from student.models import Student

# -----------------------------
# Class & Section
# -----------------------------
class ClassSection(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Class Section"
        verbose_name_plural = "Class Sections"
        unique_together = ('class_name', 'section')
        ordering = ['class_name', 'section']

    def __str__(self):
        return f"{self.class_name} - {self.section}"


# -----------------------------
# Subject
# -----------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name="subjects")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        unique_together = ('name', 'class_section')
        ordering = ['class_section', 'name']

    def __str__(self):
        return f"{self.name} ({self.class_section})"


# -----------------------------
# Teacher
# -----------------------------
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name="teachers")
    class_section = models.ForeignKey(ClassSection, on_delete=models.SET_NULL, null=True, blank=True)
    joined_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.subject.name if self.subject else 'No Subject'})"


# -----------------------------
# Attendance
# -----------------------------
class Attendance(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default="Present"
    )

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance Records"
        unique_together = ('class_section', 'subject', 'student', 'date')
        ordering = ['-date']

    def __str__(self):
        roll = getattr(self.student, 'roll_number', 'N/A')
        return f"{self.student.name} (Roll {roll}) - {self.subject.name} - {self.date} ({self.status})"


# -----------------------------
# Homework
# -----------------------------
class Homework(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.subject.name} - {self.class_section} (Due: {self.due_date})"


# -----------------------------
# Exam
# -----------------------------
class Exam(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    max_marks = models.PositiveIntegerField()
    syllabus = models.TextField()

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ['exam_date']

    def __str__(self):
        return f"{self.subject.name} - {self.class_section} ({self.exam_date})"


# -----------------------------
# Performance
# -----------------------------
class Performance(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='performances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    remarks = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Performance"
        verbose_name_plural = "Performances"
        ordering = ['student', 'subject']
        unique_together = ('student', 'subject')

    def __str__(self):
        roll = getattr(self.student, 'roll_number', 'N/A')
        return f"{self.student.name} (Roll {roll}) - {self.subject.name}: {self.marks} Marks"
