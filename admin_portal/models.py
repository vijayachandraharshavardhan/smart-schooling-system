from django.db import models
from django.contrib.auth.models import User

# -------------------------
# Class Model
# -------------------------
class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.section}"


# -------------------------
# Student Model
# -------------------------
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    class_assigned = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return f"{self.name} ({self.roll_number})"


# -------------------------
# Teacher Model
# -------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    classes = models.ManyToManyField(Class, related_name="teachers")

    def __str__(self):
        return self.name


# -------------------------
# Announcement Model
# -------------------------
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -------------------------
# Homework Model
# -------------------------
class Homework(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    class_assigned = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="homeworks"
    )

    def __str__(self):
        return self.title


# -------------------------
# Performance Model
# -------------------------
class Performance(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="performances"
    )
    subject = models.CharField(max_length=100)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.marks_obtained}/{self.total_marks}"

    def percentage(self):
        if self.total_marks > 0:
            return (self.marks_obtained / self.total_marks) * 100
        return 0


# -------------------------
# About Info Model
# -------------------------
class AboutInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# -------------------------
# Result Info Model
# -------------------------
class ResultInfo(models.Model):
    exam_name = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    summary = models.TextField()
    pdf = models.FileField(upload_to="results/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exam_name} ({self.year})"


# -------------------------
# Contact Info Model
# -------------------------
class ContactInfo(models.Model):
    school_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    map_embed = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Info - {self.school_name}"
